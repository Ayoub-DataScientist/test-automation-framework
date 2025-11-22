"""
Custom assertions for the test framework.
"""

import requests


def assert_status_code(response: requests.Response, expected_status: int, message: str = ""):
    """
    Assert that response status code matches expected value.
    
    Args:
        response: Response object
        expected_status: Expected status code
        message: Optional custom message
    """
    assert response.status_code == expected_status, \
        f"{message} Expected status {expected_status}, got {response.status_code}"


def assert_response_contains_key(response: dict, key: str, message: str = ""):
    """
    Assert that response contains a specific key.
    
    Args:
        response: Response dictionary
        key: Key to check
        message: Optional custom message
    """
    assert key in response, f"{message} Key '{key}' not found in response"


def assert_response_value(response: dict, key: str, expected_value, message: str = ""):
    """
    Assert that response value matches expected value.
    
    Args:
        response: Response dictionary
        key: Key to check
        expected_value: Expected value
        message: Optional custom message
    """
    assert response.get(key) == expected_value, \
        f"{message} Expected {key}={expected_value}, got {response.get(key)}"


def assert_element_visible(page, selector: str, message: str = ""):
    """
    Assert that element is visible on page.
    
    Args:
        page: Playwright page object
        selector: Element selector
        message: Optional custom message
    """
    assert page.is_visible(selector), \
        f"{message} Element '{selector}' is not visible"


def assert_element_enabled(page, selector: str, message: str = ""):
    """
    Assert that element is enabled.
    
    Args:
        page: Playwright page object
        selector: Element selector
        message: Optional custom message
    """
    assert page.is_enabled(selector), \
        f"{message} Element '{selector}' is not enabled"


def assert_url_contains(page, expected_url: str, message: str = ""):
    """
    Assert that current URL contains expected string.
    
    Args:
        page: Playwright page object
        expected_url: Expected URL substring
        message: Optional custom message
    """
    assert expected_url in page.url, \
        f"{message} Expected URL to contain '{expected_url}', got '{page.url}'"


def assert_text_visible(page, text: str, message: str = ""):
    """
    Assert that text is visible on page.
    
    Args:
        page: Playwright page object
        text: Text to find
        message: Optional custom message
    """
    assert page.get_by_text(text).is_visible(), \
        f"{message} Text '{text}' not found on page"
