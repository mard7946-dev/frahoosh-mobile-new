import json
from pathlib import Path

SESSION_FILE = Path(__file__).resolve().parent.parent / "storage" / "session.json"


def save_session(data: dict):
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def load_session():
    try:
        return json.loads(SESSION_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def clear_session():
    try:
        SESSION_FILE.unlink()
    except FileNotFoundError:
        pass
