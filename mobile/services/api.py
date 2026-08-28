from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

from mobile.config import (
    SUPABASE_URL,
    SUPABASE_ANON_KEY,
    SCHOOL_ID,
    API_TIMEOUT,
)


class ApiError(RuntimeError):
    pass


class _Response:
    def __init__(self, status, body):
        self.status_code = status
        self._body = body

    @property
    def ok(self):
        return 200 <= self.status_code < 300

    def json(self):
        if not self._body:
            return {}
        return json.loads(self._body.decode("utf-8"))

    def text(self):
        return self._body.decode("utf-8", errors="replace")


def _request(
    method,
    url,
    headers=None,
    payload=None,
    params=None,
    timeout=15,
):
    if params:
        url += ("&" if "?" in url else "?") + urlencode(params)

    data = None
    req_headers = headers or {}

    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        req_headers = {
            **req_headers,
            "Content-Type": "application/json",
        }

    request = Request(
        url,
        data=data,
        headers=req_headers,
        method=method,
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            return _Response(
                response.status,
                response.read(),
            )

    except HTTPError as exc:
        body = exc.read()

        return _Response(
            exc.code,
            body,
        )

    except URLError as exc:
        raise ApiError(
            f"خطای اتصال به سرور: {exc.reason}"
        ) from exc

    except TimeoutError as exc:
        raise ApiError(
            "زمان اتصال به سرور به پایان رسید."
        ) from exc


class SupabaseClient:

    def __init__(self):
        self.url = SUPABASE_URL
        self.key = SUPABASE_ANON_KEY

        self.access_token = ""
        self.refresh_token = ""

    @property
    def configured(self):
        return bool(
            self.url and
            self.key
        )

    def _headers(self, authenticated=False):

        headers = {
            "apikey": self.key,
            "Content-Type": "application/json",
        }

        if authenticated and self.access_token:
            headers[
                "Authorization"
            ] = f"Bearer {self.access_token}"

        return headers

    def sign_in(self, identifier, password):

        if not self.configured:
            raise ApiError(
                "اتصال سرور هنوز در تنظیمات برنامه فعال نشده است."
            )

        response = _request(
            "POST",
            f"{self.url}/auth/v1/token?grant_type=password",
            headers=self._headers(),
            payload={
                "email": identifier,
                "password": password,
            },
            timeout=API_TIMEOUT,
        )

        if not response.ok:

            try:
                payload = response.json()

                message = (
                    payload.get("msg")
                    or payload.get("error_description")
                    or "ورود ناموفق بود."
                )

            except Exception:
                message = "ورود ناموفق بود."

            raise ApiError(message)

        data = response.json()

        self.access_token = data.get(
            "access_token",
            "",
        )

        self.refresh_token = data.get(
            "refresh_token",
            "",
        )

        user = data.get("user") or {}

        profile = self._profile(user)

        return {
            "user": user,
            "profile": profile,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
        }

    def _profile(self, user):

        uid = user.get("id")

        if not uid:
            return {}

        try:

            response = _request(
                "GET",
                f"{self.url}/rest/v1/account_settings",
                headers={
                    **self._headers(True),
                    "Prefer": "return=representation",
                },
                params={
                    "email": f"eq.{user.get('email', '')}",
                    "limit": "1",
                },
                timeout=API_TIMEOUT,
            )

            if response.ok:

                rows = response.json()

                if rows:
                    return rows[0]

        except Exception:
            pass

        email = user.get(
            "email",
            "",
        )

        return {
            "email": email,
            "username": email,
            "display_name": email,
        }

    def table_select(
        self,
        table,
        params=None,
    ):

        if (
            not self.configured
            or not self.access_token
        ):
            raise ApiError(
                "نشست معتبر نیست."
            )

        response = _request(
            "GET",
            f"{self.url}/rest/v1/{table}",
            headers=self._headers(True),
            params=params or {
                "select": "*",
                "limit": "50",
            },
            timeout=API_TIMEOUT,
        )

        if not response.ok:
            raise ApiError(
                self._error(response)
            )

        return response.json()

    def _error(self, response):

        try:

            payload = response.json()

            return (
                payload.get("message")
                or payload.get("hint")
                or payload.get("details")
                or "خطای سرور"
            )

        except Exception:

            return (
                f"خطای سرور "
                f"({response.status_code})"
            )

    def sign_out(self):

        if (
            self.configured
            and self.access_token
        ):

            try:

                _request(
                    "POST",
                    f"{self.url}/auth/v1/logout",
                    headers=self._headers(True),
                    timeout=API_TIMEOUT,
                )

            except Exception:
                pass

        self.access_token = ""
        self.refresh_token = ""
