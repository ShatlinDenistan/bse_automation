from base.page_base import PageBase


class LoginPO(PageBase):

    # region General Login Section

    @property
    def email_textbox(self):
        selector = "//input[@placeholder='Email']"
        return self.locator(selector, "Email Textbox")

    @property
    def password_textbox(self):
        selector = "//input[@placeholder='Password']"
        return self.locator(selector, "Password Textbox")

    @property
    def login_button(self):
        selector = "(//button[contains(text(),'Login')])[2]"
        return self.locator(selector, "Login Button")

    # region Fin-Portal Specific Section

    @property
    def fin_portal_login_heading(self):
        selector = "//div[contains(text(),'Log In User')]"
        return self.locator(selector, "Fin Portal Login Heading")

    @property
    def fin_portal_username_input(self):
        selector = "//body/div[2]/div[1]/div[2]/form[1]/div[1]/input[1]"
        return self.locator(selector, "Fin Portal Username Input")

    @property
    def fin_portal_password_input(self):
        selector = "//body/div[2]/div[1]/div[2]/form[1]/div[2]/input[1]"
        return self.locator(selector, "Fin Portal Password Input")

    @property
    def fin_portal_login_button(self):
        selector = "//body/div[2]/div[1]/div[3]/button[1]"
        return self.locator(selector, "Fin Portal Login Button")

    # region CS-Admin Specific Section

    @property
    def cs_admin_email_input(self):
        selector = "//input[@name='email']"
        return self.locator(selector, "CS Admin Email Input")

    @property
    def cs_admin_password_input(self):
        selector = "//input[@name='password']"
        return self.locator(selector, "CS Admin Password Input")

    @property
    def cs_admin_login_button(self):
        selector = "//*[@class='ui green basic button']"
        return self.locator(selector, "CS Admin Login Button")
