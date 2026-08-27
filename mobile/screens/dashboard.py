from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from mobile.config import APP_NAME, SYSTEM_TITLE, PRIMARY, SECONDARY, SUCCESS, WHITE

ROLE_LABELS = {
    "manager": "مدیریت", "admin": "مدیریت", "مدیر": "مدیریت", "executive": "کادر اجرایی",
    "teacher": "دبیر", "advisor": "مشاور", "student": "دانش‌آموز", "parent": "ولی", "parent_guardian": "ولی",
}


class DashboardScreen(Screen):
    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state
        self.root = BoxLayout(orientation="vertical", padding=dp(18), spacing=dp(12))
        self.header = Label(size_hint_y=None, height=dp(75), font_size="22sp", color=PRIMARY)
        self.root.add_widget(self.header)
        self.grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, row_default_height=dp(58))
        self.root.add_widget(self.grid)
        self.add_widget(self.root)
        self.refresh()

    def refresh(self):
        self.grid.clear_widgets()
        role = self.app_state.role
        label = ROLE_LABELS.get(role, role)
        self.header.text = f"{APP_NAME}\n{self.app_state.display_name} — {label}"
        items = [
            ("تابلو هوشمند", self.open_update),
            ("اطلاعیه‌ها", self.open_update),
            ("برنامه و کلاس‌ها", self.open_update),
            ("گزارش‌ها", self.open_update),
        ]
        for text, callback in items:
            b = Button(text=text, background_normal="", background_color=SECONDARY, color=WHITE)
            b.bind(on_release=callback)
            self.grid.add_widget(b)
        update = Button(text="مرکز به‌روزرسانی", background_normal="", background_color=SUCCESS, color=WHITE)
        update.bind(on_release=self.open_update)
        self.grid.add_widget(update)
        out = Button(text="خروج", background_normal="", background_color=PRIMARY, color=WHITE)
        out.bind(on_release=self.logout)
        self.grid.add_widget(out)

    def open_update(self, *_):
        self.manager.current = "update"

    def logout(self, *_):
        self.app_state.logout()
        self.manager.current = "login"

