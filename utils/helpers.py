"""
Helper utility functions.
"""

import time
from typing import Callable, Any


def retry(func: Callable, max_attempts: int = 3, delay: float = 1.0) -> Any:
    """
    Retry a function with exponential backoff.
    
    Args:
        func: Function to retry
        max_attempts: Maximum number of attempts
        delay: Initial delay between attempts
    
    Returns:
        Function result
    """
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            time.sleep(delay * (2 ** attempt))


def wait_until(condition: Callable, timeout: int = 10, poll_frequency: float = 0.5) -> bool:
    """
    Wait until a condition is true.
    
    Args:
        condition: Condition function to check
        timeout: Maximum wait time in seconds
        poll_frequency: How often to check condition
    
    Returns:
        True if condition met, False if timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        if condition():
            return True
        time.sleep(poll_frequency)
    return False


def get_nested_value(dictionary: dict, keys: list, default=None) -> Any:
    """
    Get nested value from dictionary.
    
    Args:
        dictionary: Dictionary to search
        keys: List of keys to traverse
        default: Default value if not found
    
    Returns:
        Value or default
    """
    value = dictionary
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        else:
            return default
    return value if value is not None else default
