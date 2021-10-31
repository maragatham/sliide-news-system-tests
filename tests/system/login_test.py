from unittest import TestCase
from uiautomator import device as d

class LoginTest(TestCase):
    # Helper Methods
    # --------------

    # Enter Home Screen
    def refresh(self):
        d.press("home")
        d.press("back")

    # Close last running application
    def closeapp(self):
        d.press.home()
        d.press.recent()
        d.swipe(50, 1500, 50, 100, 10)
        d.wait.update()
        d.press.home()

    # Open News App
    def openapp(self):
        d.swipe(50, 1500, 50, 100, 10)
        d(text="News").click()
        d.wait.update()

    # Enter and submit Creds
    def enter_credentials(self, uservalue, passwordvalue):
        txtUser = d().child(text="User name")
        txtUser.clear_text()
        txtUser.set_text(uservalue)
        txtPass = d().child(text="Password")
        txtPass.clear_text()
        txtPass.set_text(passwordvalue)
        btnLogin = d().child(text="LOGIN")
        btnLogin.click()
        d.wait.update()

    # Restart App
    def freshStartApp(self):
        self.closeapp()
        self.refresh()
        self.openapp()

    # Begin Tests
    # -----------

    def test_first_time_login(self):
        self.freshStartApp()
        with self.subTest():
            self.assertTrue(d().child(text="LOGIN").exists)
        with self.subTest():
            self.assertTrue(d().child(text="Password").exists)
        with self.subTest():
            self.assertTrue(d().child(text="User name").exists)

    def test_invalid_credentials(self):
        self.freshStartApp()

        # Enter correct credentials
        self.enter_credentials("invaliduser","invalidpassword")

        # Check if we are still in Login screen
        self.assertTrue(d().child(text="LOGIN").exists)

    def test_valid_credentials(self):
        self.freshStartApp()

        # Enter wrong credentials
        self.enter_credentials("user", "password")

        # Check if we are not in Login screen
        self.assertFalse(d().child(text="LOGIN").exists)

    def test_open_app_next_time(self):
        self.freshStartApp()

        # Check if we are not in Login screen
        self.assertFalse(d().child(text="LOGIN").exists)
