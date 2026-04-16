import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestAccessValidation:
    """
    AccessGuard - Automated Role-Based Access Validation Suite
    Tests login functionality and role-based access controls
    """

    def test_valid_admin_login(self, driver, base_url):
        """Admin should be able to log in successfully"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert login_page.is_login_successful(), "Admin login failed!"

    def test_invalid_login_rejected(self, driver, base_url):
        """Invalid credentials should be rejected"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("wronguser", "wrongpassword")
        assert login_page.is_login_failed(), "Invalid login was not rejected!"

    def test_empty_credentials_rejected(self, driver, base_url):
        """Empty credentials should not allow login"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("", "")
        assert login_page.is_login_failed(), "Empty credentials were accepted!"

    def test_valid_login_then_secure_area_accessible(self, driver, base_url):
        """After login, secure area should be accessible"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert "secure" in driver.current_url, "Not redirected to secure area!"

    def test_read_only_cannot_access_admin(self, driver, base_url):
        """Read-only user should not access admin features"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("wronguser", "wrongpassword")
        dashboard = DashboardPage(driver)
        assert not dashboard.can_access_admin_panel(), (
            "SECURITY VIOLATION: Unauthorized user has admin access!"
        )

    def test_cross_browser_login_works(self, driver, base_url):
        """Login should work consistently across browsers"""
        driver.get(f"{base_url}/login")
        login_page = LoginPage(driver)
        login_page.login("tomsmith", "SuperSecretPassword!")
        assert login_page.is_login_successful(), (
            f"Login failed on {driver.capabilities['browserName']}"
        )
