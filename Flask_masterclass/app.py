import time

from flask import Flask, jsonify
from sqlalchemy import event
from sqlalchemy.orm import joinedload

from config import config
from models import db, Booking


app = Flask(__name__)

# Wczytanie konfiguracji developerskiej
app.config.from_object(config['development'])

# Połączenie SQLAlchemy z aplikacją Flask
db.init_app(app)


# ============================================================
# STRONA GŁÓWNA
# ============================================================

@app.route('/')
def index():
    return "Flask + PostgreSQL działa! 🎉"


# ============================================================
# TEST POŁĄCZENIA Z BAZĄ
# ============================================================

@app.route('/test-db')
def test_db():
    """Testuje połączenie z bazą danych."""

    try:
        db.session.execute(db.text('SELECT 1'))
        return "✅ Połączenie z PostgreSQL OK!"

    except Exception as e:
        return f"❌ Błąd połączenia: {str(e)}"


# ============================================================
# ZADANIE 2 - PROBLEM N+1
# ============================================================

@app.route('/debug/n-plus-1')
def debug_n_plus_1():
    """
    Porównuje:
    1. Pobieranie rezerwacji bez optymalizacji
    2. Pobieranie rezerwacji z joinedload()
    """

    results = {}

    # Licznik wszystkich zapytań SQL
    query_count = 0

    def count_query(
        conn,
        cursor,
        statement,
        parameters,
        context,
        executemany
    ):
        nonlocal query_count
        query_count += 1

    # Listener uruchamia count_query przed każdym zapytaniem SQL
    event.listen(
        db.engine,
        'before_cursor_execute',
        count_query
    )

    try:

        # ====================================================
        # 1. BEZ OPTYMALIZACJI
        # ====================================================

        # Czyścimy sesję SQLAlchemy
        db.session.remove()

        # Zerujemy licznik
        query_count = 0

        # Start pomiaru czasu
        start = time.perf_counter()

        # Pobieramy tylko Booking
        bookings = Booking.query.all()

        bookings_data = []

        for booking in bookings:
            bookings_data.append({
                'id': booking.id,
                'title': booking.title,

                # Te odwołania mogą powodować dodatkowe zapytania
                'room': booking.room.name,
                'user': booking.user.name
            })

        # Koniec pomiaru czasu
        elapsed = time.perf_counter() - start

        results['without_optimization'] = {
            'query_count': query_count,
            'time_seconds': round(elapsed, 6),
            'bookings': bookings_data
        }

        # ====================================================
        # 2. Z OPTYMALIZACJĄ joinedload()
        # ====================================================

        # Czyścimy sesję, aby drugi test był niezależny
        db.session.remove()

        # Zerujemy licznik
        query_count = 0

        # Start pomiaru czasu
        start = time.perf_counter()

        # Pobieramy Booking razem z Room i User
        bookings = Booking.query.options(
            joinedload(Booking.room),
            joinedload(Booking.user)
        ).all()

        optimized_data = []

        for booking in bookings:
            optimized_data.append({
                'id': booking.id,
                'title': booking.title,
                'room': booking.room.name,
                'user': booking.user.name
            })

        elapsed = time.perf_counter() - start

        results['with_joinedload'] = {
            'query_count': query_count,
            'time_seconds': round(elapsed, 6),
            'bookings': optimized_data
        }

    finally:

        # Odpinamy listener po zakończeniu testu
        event.remove(
            db.engine,
            'before_cursor_execute',
            count_query
        )

    # ========================================================
    # PORÓWNANIE
    # ========================================================

    results['comparison'] = {
        'queries_saved': (
            results['without_optimization']['query_count']
            - results['with_joinedload']['query_count']
        )
    }

    return jsonify(results)


# ============================================================
# START APLIKACJI
# ============================================================

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        print("✅ Tabele utworzone!")

    app.run(debug=True)