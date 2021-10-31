from unittest import TestCase
from uiautomator import device as d

class LoginTest(TestCase):
    def refresh(self):
        d.press("home")
        d.press("back")

    def closeapp(self):
        d.press.home()
        d.press.recent()
        d.swipe(50, 1500, 50, 100, 10)
        d.wait.update()
        d.press.home()

    def openapp(self):
        d.swipe(50, 1500, 50, 100, 10)
        d(text="News").click()
        d.wait.update()

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

    def test_first_time_login(self):
        self.closeapp()
        self.refresh()
        self.openapp()
        with self.subTest():
            self.assertTrue(d().child(text="LOGIN").exists)
        with self.subTest():
            self.assertTrue(d().child(text="Password").exists)
        with self.subTest():
            self.assertTrue(d().child(text="User name").exists)

    def test_invalid_credentials(self):
        self.closeapp()
        self.refresh()
        self.openapp()

        # Enter correct credentials
        self.enter_credentials("invaliduser","invalidpassword")

        # Check if we are still in Login screen
        self.assertTrue(d().child(text="LOGIN").exists)

    def test_valid_credentials(self):
        self.closeapp()
        self.refresh()
        self.openapp()

        # Enter wrong credentials
        self.enter_credentials("user", "password")

        # Check if we are not in Login screen
        self.assertFalse(d().child(text="LOGIN").exists)


    def test_open_app_next_time(self):
        self.closeapp()
        self.refresh()
        self.openapp()

        # Check if we are not in Login screen
        self.assertFalse(d().child(text="LOGIN").exists)
