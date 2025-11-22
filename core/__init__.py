"""
Core framework components.
"""

from core.logger import get_logger
from core.base_test import BaseTest
from core.assertions import (
    assert_status_code,
    assert_response_contains_key,
    assert_element_visible,
)

__all__ = [
    "get_logger",
    "BaseTest",
    "assert_status_code",
    "assert_response_contains_key",
    "assert_element_visible",
]
