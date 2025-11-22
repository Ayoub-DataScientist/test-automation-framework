"""
Base test class for all tests.
"""

import pytest
from core.logger import get_logger


class BaseTest:
    """Base class for all tests."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for each test."""
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"Starting test: {self._get_test_name()}")
        yield
        self.logger.info(f"Completed test: {self._get_test_name()}")
    
    def _get_test_name(self) -> str:
        """Get the current test name."""
        return getattr(self, '_testMethodName', 'unknown')
