from mobile.services.api import SupabaseClient
from mobile.services.session import load_session, save_session, clear_session


class AppState:
    def __init__(self):
        self.api = SupabaseClient()
        self.session = load_session()
        if self.session:
            self.api.access_token = self.session.get("access_token", "")
            self.api.refresh_token = self.session.get("refresh_token", "")

    @property
    def logged_in(self):
        return bool(self.session and self.api.access_token)

    @property
    def profile(self):
        return (self.session or {}).get("profile") or {}

    @property
    def role(self):
        return str(self.profile.get("role") or "student").strip().lower()

    @property
    def display_name(self):
        return self.profile.get("display_name") or self.profile.get("username") or "کاربر فراهوش"

    def set_session(self, payload):
        self.session = payload
        save_session(payload)
        self.api.access_token = payload.get("access_token", "")
        self.api.refresh_token = payload.get("refresh_token", "")

    def logout(self):
        self.api.sign_out()
        clear_session()
        self.session = None
