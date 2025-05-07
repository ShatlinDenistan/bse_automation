from pos.login_po import LoginPO


class LoginPage(LoginPO):
    """Page methods and elements for login page"""

    def confirm_if_in_page(self):
        """Confirm if in login page"""
        self.expect_to_be_visible(self.login_button)

    def login(self, username, password):
        """login into the system"""
        self.logger.info("Pre-requisite: Login to the system")
        self.fill(self.email_textbox, username)
        self.fill(self.password_textbox, password)
        self.click(self.login_button)

    def login_fin_portal(self, username, password):
        """
        Login to Fin-Portal

        Args:
            username: Username for Fin-Portal
            password: Password for Fin-Portal
        """
        # Wait for the login element to be visible
        self.fin_portal_login_heading.wait_for(state="visible")

        # Fill in credentials
        self.fin_portal_username_input.fill(username)
        self.fin_portal_password_input.fill(password)

        # Click login button
        self.fin_portal_login_button.click()

        # Wait for login to complete
        self.wait_for_seconds(5)

    def login_cs_admin(self, username, password):
        """
        Login to CS-Admin

        Args:
            username: Username for CS-Admin
            password: Password for CS-Admin
        """
        # Wait for the login element to be visible
        self.cs_admin_email_input.wait_for(state="visible")

        # Fill in credentials
        self.cs_admin_email_input.fill(username)
        self.cs_admin_password_input.fill(password)

        # Click login button
        self.cs_admin_login_button.click()

        # Wait for login to complete
        self.wait_for_seconds(5)
