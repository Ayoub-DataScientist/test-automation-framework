"""
Base page object for all UI pages.
"""

from playwright.sync_api import Page
from config import get_config
from core.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, page: Page, config=None):
        """Initialize page object."""
        self.page = page
        self.config = config or get_config()
        self.base_url = self.config.BASE_URL
        self.logger = get_logger(self.__class__.__name__)
    
    def navigate(self, path: str = ""):
        """Navigate to a specific path."""
        url = f"{self.base_url}{path}"
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url, wait_until="networkidle")
    
    def fill(self, selector: str, text: str):
        """Fill a text field."""
        self.logger.debug(f"Filling {selector} with {text}")
        self.page.fill(selector, text)
    
    def click(self, selector: str):
        """Click an element."""
        self.logger.debug(f"Clicking {selector}")
        self.page.click(selector)
    
    def get_text(self, selector: str) -> str:
        """Get text from element."""
        text = self.page.text_content(selector) or ""
        self.logger.debug(f"Got text from {selector}: {text}")
        return text
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        visible = self.page.is_visible(selector)
        self.logger.debug(f"Element {selector} visible: {visible}")
        return visible
    
    def wait_for_navigation(self):
        """Wait for page navigation."""
        self.logger.debug("Waiting for navigation")
        self.page.wait_for_load_state("networkidle")
