from unittest import TestCase
from uiautomator import device as d


class NewsTest(TestCase):
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

    def freshlogin(self):
        self.closeapp()
        self.refresh()
        self.openapp()
        self.enter_credentials("user", "password")

    def disablenetwork(self):
        pass

    # Tests

    def test_image_loaded(self):
        self.freshlogin()
        self.assertFalse(d().child(text="Failed to load news").info)

    def test_without_internet(self):
        self.disablenetwork()
        self.freshlogin()
        self.assertTrue(d().child(text="Failed to load news").exists)


