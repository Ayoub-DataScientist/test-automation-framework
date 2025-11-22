"""
Example API tests demonstrating framework usage.
"""

import pytest
from core.base_test import BaseTest
from core.assertions import assert_status_code
from api.base_api_client import BaseAPIClient


class TestExampleAPI(BaseTest):
    """Example API test suite."""
    
    @pytest.mark.smoke
    @pytest.mark.api
    def test_api_health_check(self):
        """Test API health check endpoint."""
        api = BaseAPIClient()
        response = api.get("/health")
        assert_status_code(response, 200)
        self.logger.info("API health check passed")
        api.close()
    
    @pytest.mark.regression
    @pytest.mark.api
    def test_api_response_structure(self):
        """Test API response structure."""
        api = BaseAPIClient()
        response = api.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        self.logger.info(f"API response: {data}")
        api.close()
