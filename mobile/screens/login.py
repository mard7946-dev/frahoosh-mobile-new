from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp
from mobile.config import APP_NAME, SYSTEM_TITLE, SCHOOL_NAME, PRIMARY, SECONDARY, SUCCESS, WHITE, BACKGROUND


class LoginScreen(Screen):
    def __init__(self, app_state, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state
        root = BoxLayout(orientation="vertical", padding=dp(24), spacing=dp(16))
        root.add_widget(Label(text=APP_NAME, font_size="34sp", bold=True, color=PRIMARY, size_hint_y=None, height=dp(55)))
        root.add_widget(Label(text=SYSTEM_TITLE, font_size="18sp", color=SECONDARY, size_hint_y=None, height=dp(35)))
        root.add_widget(Label(text=SCHOOL_NAME, font_size="14sp", color=PRIMARY, size_hint_y=None, height=dp(32)))
        card = BoxLayout(orientation="vertical", spacing=dp(12), padding=dp(18), size_hint_y=None, height=dp(300))
        self.identifier = TextInput(hint_text="ایمیل کاربر", multiline=False, write_tab=False, size_hint_y=None, height=dp(52))
        self.password = TextInput(hint_text="رمز عبور", password=True, multiline=False, write_tab=False, size_hint_y=None, height=dp(52))
        self.status = Label(text="", color=SECONDARY, size_hint_y=None, height=dp(36))
        button = Button(text="ورود به فراهوش", background_normal="", background_color=SUCCESS, color=WHITE, size_hint_y=None, height=dp(54))
        button.bind(on_release=self.login)
        card.add_widget(self.identifier); card.add_widget(self.password); card.add_widget(self.status); card.add_widget(button)
        root.add_widget(card)
        root.add_widget(Label(text="برای ورود آنلاین، URL و کلید عمومی Supabase باید در تنظیمات Build قرار گرفته باشد.", font_size="12sp", color=SECONDARY))
        self.add_widget(root)

    def login(self, *_):
        identifier = self.identifier.text.strip()
        password = self.password.text
        if not identifier or not password:
            self.status.text = "ایمیل و رمز عبور را وارد کنید."
            return
        self.status.text = "در حال اتصال به سرور..."
        try:
            payload = self.app_state.api.sign_in(identifier, password)
            self.app_state.set_session(payload)
            self.manager.get_screen("dashboard").refresh()
            self.manager.current = "dashboard"
        except Exception as exc:
            self.status.text = str(exc)


