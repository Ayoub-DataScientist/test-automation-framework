"""
Pytest configuration and fixtures.
"""

import pytest
from playwright.sync_api import sync_playwright
from config import get_config


def pytest_addoption(parser):
    """Add custom command-line options."""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment: dev, staging, or prod",
    )


@pytest.fixture(scope="session")
def config(request):
    """Provide configuration."""
    env = request.config.getoption("--env")
    return get_config(env)


@pytest.fixture
def browser(config):
    """Provide Playwright browser."""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=config.HEADLESS)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser):
    """Provide Playwright page."""
    page = browser.new_page()
    yield page
    page.close()


def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "ui: UI tests")
    config.addinivalue_line("markers", "api: API tests")
