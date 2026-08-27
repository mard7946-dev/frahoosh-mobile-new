import requests
from mobile.config import SUPABASE_URL, SUPABASE_ANON_KEY, SCHOOL_ID, API_TIMEOUT


class ApiError(RuntimeError):
    pass


class SupabaseClient:
    def __init__(self):
        self.url = SUPABASE_URL
        self.key = SUPABASE_ANON_KEY
        self.access_token = ""
        self.refresh_token = ""

    @property
    def configured(self):
        return bool(self.url and self.key)

    def _headers(self, authenticated=False):
        headers = {
            "apikey": self.key,
            "Content-Type": "application/json",
        }
        if authenticated and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def sign_in(self, identifier, password):
        if not self.configured:
            raise ApiError("اتصال سرور هنوز در تنظیمات برنامه فعال نشده است.")
        response = requests.post(
            f"{self.url}/auth/v1/token?grant_type=password",
            headers=self._headers(),
            json={"email": identifier, "password": password},
            timeout=API_TIMEOUT,
        )
        if not response.ok:
            try:
                message = response.json().get("msg") or response.json().get("error_description") or "ورود ناموفق بود."
            except Exception:
                message = "ورود ناموفق بود."
            raise ApiError(message)
        data = response.json()
        self.access_token = data.get("access_token", "")
        self.refresh_token = data.get("refresh_token", "")
        user = data.get("user") or {}
        profile = self._profile(user)
        return {"user": user, "profile": profile, "access_token": self.access_token, "refresh_token": self.refresh_token}

    def _profile(self, user):
        uid = user.get("id")
        if not uid:
            return {}
        # The v16.12 schema contains account_settings and school users are
        # identified by username. We query account_settings when available.
        try:
            response = requests.get(
                f"{self.url}/rest/v1/account_settings",
                headers={**self._headers(True), "Prefer": "return=representation"},
                params={"email": f"eq.{user.get('email', '')}", "limit": 1},
                timeout=API_TIMEOUT,
            )
            if response.ok:
                rows = response.json()
                if rows:
                    return rows[0]
        except requests.RequestException:
            pass
        return {"email": user.get("email", ""), "username": user.get("email", ""), "display_name": user.get("email", "")}

    def table_select(self, table, params=None):
        if not self.configured or not self.access_token:
            raise ApiError("نشست معتبر نیست.")
        response = requests.get(
            f"{self.url}/rest/v1/{table}",
            headers=self._headers(True),
            params=params or {"select": "*", "limit": "50"},
            timeout=API_TIMEOUT,
        )
        if not response.ok:
            raise ApiError(self._error(response))
        return response.json()

    def _error(self, response):
        try:
            payload = response.json()
            return payload.get("message") or payload.get("hint") or payload.get("details") or "خطای سرور"
        except Exception:
            return f"خطای سرور ({response.status_code})"

    def sign_out(self):
        if self.configured and self.access_token:
            try:
                requests.post(f"{self.url}/auth/v1/logout", headers=self._headers(True), timeout=API_TIMEOUT)
            except requests.RequestException:
                pass
        self.access_token = ""
        self.refresh_token = ""
