import os


# ============================================================
# Frahoosh Mobile Configuration
# ============================================================

APP_NAME = "فراهوش"
SYSTEM_TITLE = "سامانه هوشمند آموزشی یکپارچه"
APP_VERSION = "1.0.0"

PACKAGE_NAME = "ir.frahoosh"
DEVELOPER_NAME = "تیم توسعه فراهوش"


# ============================================================
# Supabase
# ============================================================

SUPABASE_URL = os.getenv(
    "FRAHOOSH_SUPABASE_URL",
    ""
).strip().rstrip("/")

SUPABASE_ANON_KEY = os.getenv(
    "FRAHOOSH_SUPABASE_ANON_KEY",
    ""
).strip()

SCHOOL_ID = os.getenv(
    "FRAHOOSH_SCHOOL_ID",
    "frahoosh-school"
)

API_TIMEOUT = float(
    os.getenv(
        "FRAHOOSH_API_TIMEOUT",
        "15"
    )
)


# ============================================================
# School
# ============================================================

SCHOOL_NAME = os.getenv(
    "FRAHOOSH_SCHOOL_NAME",
    "دبیرستان سردار شهید حاجی‌زاده ۲"
)

SCHOOL_YEAR = os.getenv(
    "FRAHOOSH_SCHOOL_YEAR",
    "۱۴۰۵ - ۱۴۰۶"
)

SCHOOL_LOGO = "assets/frahoosh_logo.png"


# ============================================================
# UI Colors
# ============================================================

PRIMARY = (
    0.059,
    0.09,
    0.165,
    1
)

SECONDARY = (
    0.118,
    0.227,
    0.545,
    1
)

SUCCESS = (
    0.086,
    0.639,
    0.325,
    1
)

BACKGROUND = (
    0.973,
    0.98,
    0.988,
    1
)

WHITE = (
    1,
    1,
    1,
    1
)

TEXT = (
    0.08,
    0.10,
    0.14,
    1
)

MUTED = (
    0.38,
    0.42,
    0.48,
    1
)

ERROR = (
    0.75,
    0.12,
    0.12,
    1
)

