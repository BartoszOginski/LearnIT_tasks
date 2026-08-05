from pathlib import Path

src = Path("Projekt") / "src"
data = Path("Projekt") / "data"
docs = Path("Projekt") / "docs"

src.mkdir(parents=True, exist_ok=True)
data.mkdir(parents=True, exist_ok=True)
docs.mkdir(parents=True, exist_ok=True)