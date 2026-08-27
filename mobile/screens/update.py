from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from mobile.config import APP_NAME, APP_VERSION, PRIMARY, SECONDARY, SUCCESS, WHITE


class UpdateScreen(Screen):
    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state
        root = BoxLayout(orientation="vertical", padding=dp(22), spacing=dp(14))
        self.title = Label(text="مرکز به‌روزرسانی فراهوش", font_size="24sp", color=PRIMARY, size_hint_y=None, height=dp(60))
        self.info = Label(font_size="15sp", color=SECONDARY)
        root.add_widget(self.title); root.add_widget(self.info)
        back = Button(text="بازگشت", background_normal="", background_color=SUCCESS, color=WHITE, size_hint_y=None, height=dp(54))
        back.bind(on_release=lambda *_: setattr(self.manager, "current", "dashboard"))
        root.add_widget(back)
        self.add_widget(root)
        self.refresh()

    def refresh(self):
        state = "متصل به Backend" if self.app_state.api.configured else "Backend هنوز پیکربندی نشده"
        self.info.text = f"نسخه نصب‌شده: {APP_VERSION}\n{state}\n\nبه‌روزرسانی‌های رسمی باید از سرور فراهوش دریافت شوند؛ هیچ نصب مجدد دستی در طراحی نهایی لازم نیست."
