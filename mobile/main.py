from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from mobile.config import APP_NAME, APP_VERSION, BACKGROUND
from mobile.services.app_state import AppState
from mobile.screens.login import LoginScreen
from mobile.screens.dashboard import DashboardScreen
from mobile.screens.update import UpdateScreen


class FrahooshMobileApp(App):

    title = APP_NAME

    def build(self):
        Window.clearcolor = BACKGROUND

        self.state = AppState()

        manager = ScreenManager(
            transition=FadeTransition(
                duration=0.12
            )
        )

        manager.add_widget(
            LoginScreen(
                self.state,
                name="login"
            )
        )

        manager.add_widget(
            DashboardScreen(
                self.state,
                name="dashboard"
            )
        )

        manager.add_widget(
            UpdateScreen(
                self.state,
                name="update"
            )
        )

        manager.current = (
            "dashboard"
            if self.state.logged_in
            else "login"
        )

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
`
