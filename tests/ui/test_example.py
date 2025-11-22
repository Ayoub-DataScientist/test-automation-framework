"""
Example UI tests demonstrating framework usage.
"""

import pytest
from core.base_test import BaseTest
from ui.base_page import BasePage


class TestExampleUI(BaseTest):
    """Example UI test suite."""
    
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_page_navigation(self, page):
        """Test basic page navigation."""
        base_page = BasePage(page)
        base_page.navigate("/")
        assert page.url  # Verify page loaded
        self.logger.info("Page navigation test passed")
    
    @pytest.mark.regression
    @pytest.mark.ui
    def test_page_title(self, page):
        """Test page title."""
        base_page = BasePage(page)
        base_page.navigate("/")
        title = page.title()
        assert title  # Verify title exists
        self.logger.info(f"Page title: {title}")
