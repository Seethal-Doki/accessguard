from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    ADMIN_PANEL = (By.ID, "admin-panel")
    APPROVE_BUTTON = (By.ID, "approve-btn")
    REPORTS_MENU = (By.ID, "reports-menu")
    TRANSFER_BUTTON = (By.ID, "transfer-btn")
    AUDIT_LOG = (By.ID, "audit-log")
    WELCOME_MESSAGE = (By.ID, "welcome-msg")

    ROLE_PERMISSIONS = {
        "admin": {"admin_panel": True, "approve": True, "reports": True, "transfer": True, "audit_log": True},
        "manager": {"admin_panel": False, "approve": True, "reports": True, "transfer": True, "audit_log": False},
        "read_only": {"admin_panel": False, "approve": False, "reports": True, "transfer": False, "audit_log": False}
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def can_access_admin_panel(self):
        return self.is_element_visible(self.ADMIN_PANEL)

    def can_access_approve(self):
        return self.is_element_visible(self.APPROVE_BUTTON)

    def can_access_reports(self):
        return self.is_element_visible(self.REPORTS_MENU)

    def can_access_transfer(self):
        return self.is_element_visible(self.TRANSFER_BUTTON)

    def can_access_audit_log(self):
        return self.is_element_visible(self.AUDIT_LOG)

    def validate_role_permissions(self, role):
        expected = self.ROLE_PERMISSIONS.get(role, {})
        return {
            "admin_panel": self.can_access_admin_panel() == expected.get("admin_panel"),
            "approve": self.can_access_approve() == expected.get("approve"),
            "reports": self.can_access_reports() == expected.get("reports"),
            "transfer": self.can_access_transfer() == expected.get("transfer"),
            "audit_log": self.can_access_audit_log() == expected.get("audit_log")
        }
