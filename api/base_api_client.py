"""
Base API client for all API endpoints.
"""

import requests
from config import get_config
from core.logger import get_logger

logger = get_logger(__name__)


class BaseAPIClient:
    """Base class for all API clients."""
    
    def __init__(self, config=None):
        """Initialize API client."""
        self.config = config or get_config()
        self.base_url = self.config.API_BASE_URL
        self.timeout = self.config.TIMEOUT
        self.verify_ssl = self.config.VERIFY_SSL
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)
    
    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        """Perform GET request."""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url}")
        return self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )
    
    def post(self, endpoint: str, json: dict = None, headers: dict = None):
        """Perform POST request."""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url}")
        return self.session.post(
            url,
            json=json,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )
    
    def put(self, endpoint: str, json: dict = None, headers: dict = None):
        """Perform PUT request."""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PUT {url}")
        return self.session.put(
            url,
            json=json,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )
    
    def delete(self, endpoint: str, headers: dict = None):
        """Perform DELETE request."""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")
        return self.session.delete(
            url,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )
    
    def close(self):
        """Close the session."""
        self.session.close()
