from .base.core_locators import CoreLocators


class GitHubPage(CoreLocators):

    def __init__(self, driver, url="https://github.com/login"):
        super().__init__(driver, url)

    @property
    def username_field(self):
        return self.XPATH("//input[@id='login_field']")

    @property
    def password_field(self):
        return self.XPATH("//input[@id='password']")

    @property
    def verification_step_fail(self):
        return self.XPATH("//div[contains(text(), 'Incorrect username or password.')]")

    @property
    def dashboard_title(self):
        return self.XPATH("//span[contains(text(), 'Dashboard')]/../../a/span")

    @property
    def login_button(self):
        return self.XPATH("//input[@value='Sign in']")

    @property
    def user_avatar(self):
        return self.XPATH("//img[@class='avatar circle']")

    @property
    def sign_out(self):
        return self.XPATH("//span[contains(text(), 'Sign out')]")

    @property
    def sign_out_submit(self):
        return self.XPATH("//input[@value='Sign out from all accounts']")

    @property
    def sign_up_button(self):
        return self.XPATH("//form[@action='/signup']//button[contains(text(), 'Sign up')]")

