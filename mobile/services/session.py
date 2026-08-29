import json
from pathlib import Path


# ============================================================
# Frahoosh Mobile Session Storage
# ============================================================

SESSION_FILE = (
    Path(__file__).resolve().parent.parent
    / "storage"
    / "session.json"
)


def save_session(data: dict):
    """
    ذخیره اطلاعات نشست کاربر.
    """

    if not isinstance(data, dict):
        data = {}

    try:
        SESSION_FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        SESSION_FILE.write_text(
            json.dumps(
                data,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    except (OSError, TypeError, ValueError):
        # خطای ذخیره Session نباید باعث Crash برنامه شود.
        pass


def load_session():
    """
    بارگذاری نشست قبلی کاربر.
    """

    try:
        if not SESSION_FILE.exists():
            return None

        data = json.loads(
            SESSION_FILE.read_text(
                encoding="utf-8"
            )
        )

        if isinstance(data, dict):
            return data

        return None

    except (
        FileNotFoundError,
        json.JSONDecodeError,
        OSError,
        UnicodeDecodeError,
        TypeError,
        ValueError,
    ):
        return None


def clear_session():
    """
    حذف نشست کاربر.
    """

    try:
        if SESSION_FILE.exists():
            SESSION_FILE.unlink()

    except OSError:
        # عدم توانایی حذف Session نباید باعث Crash شود.
        pass
```
