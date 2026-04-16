import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome or firefox"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Browser '{browser}' not supported.")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com"


@pytest.fixture(scope="session")
def test_users():
    return {
        "admin": {"username": "admin", "password": "admin123", "role": "admin"},
        "manager": {"username": "manager", "password": "manager123", "role": "manager"},
        "read_only": {"username": "readonly", "password": "readonly123", "role": "read_only"}
    }