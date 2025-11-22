# Advanced Test Automation Framework

##  Project Overview

This repository contains a **production-ready test automation framework** that combines **UI testing** (Playwright) and **API testing** (Requests) into a single, cohesive framework. It demonstrates **professional architecture**, **reusable utilities**, **comprehensive logging**, and **advanced reporting**.

**QA Skills Demonstrated:**
- Designing scalable test automation architecture
- Integrating multiple testing layers (UI + API)
- Implementing reusable utilities and helpers
- Professional logging and debugging
- Advanced test reporting and analytics
- Configuration management for different environments

---

##  Framework Architecture

The framework is organized into layers for maximum maintainability and reusability:

```
┌─────────────────────────────────────────────────────────┐
│                    Test Layer                           │
│              (UI Tests & API Tests)                     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  Page Object Layer                      │
│           (UI Pages & API Endpoints)                    │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                  Utilities Layer                        │
│   (Logging, Config, Helpers, Assertions)               │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              Third-Party Libraries                      │
│   (Playwright, Requests, Pytest, etc.)                 │
└─────────────────────────────────────────────────────────┘
```

---

##  Project Structure

```
test-automation-framework/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── pytest.ini                         # Pytest configuration
├── conftest.py                        # Pytest fixtures and hooks
├── config/                            # Configuration management
│   ├── __init__.py
│   ├── config.py                      # Base configuration
│   ├── dev.env                        # Development environment
│   └── staging.env                    # Staging environment
├── core/                              # Core framework components
│   ├── __init__.py
│   ├── logger.py                      # Logging configuration
│   ├── base_test.py                   # Base test class
│   └── assertions.py                  # Custom assertions
├── ui/                                # UI testing layer
│   ├── __init__.py
│   ├── base_page.py                   # Base page object
│   ├── pages/                         # Page objects
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── product_page.py
│   │   └── cart_page.py
│   └── locators/                      # Element locators
│       ├── __init__.py
│       └── locators.py
├── api/                               # API testing layer
│   ├── __init__.py
│   ├── base_api_client.py             # Base API client
│   ├── endpoints/                     # API endpoints
│   │   ├── __init__.py
│   │   ├── user_api.py
│   │   └── product_api.py
│   └── payloads/                      # Request payloads
│       ├── __init__.py
│       └── payloads.py
├── utils/                             # Utility functions
│   ├── __init__.py
│   ├── helpers.py                     # Helper functions
│   ├── data_generator.py              # Test data generation
│   └── wait_utils.py                  # Wait and retry logic
├── tests/                             # Test files
│   ├── __init__.py
│   ├── ui/                            # UI tests
│   │   ├── __init__.py
│   │   ├── test_authentication.py
│   │   ├── test_products.py
│   │   └── test_checkout.py
│   └── api/                           # API tests
│       ├── __init__.py
│       ├── test_users_api.py
│       └── test_products_api.py
├── reports/                           # Test reports (generated)
│   └── index.html
└── logs/                              # Test logs (generated)
    └── test_execution.log
```

---

##  Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.9+ | Test scripting |
| **UI Testing** | Playwright | Cross-browser automation |
| **API Testing** | Requests | HTTP client |
| **Test Framework** | Pytest | Test execution and reporting |
| **Logging** | Python logging | Detailed test logs |
| **Configuration** | Python-dotenv | Environment management |

---

##  Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ayoub-DataScientist/test-automation-framework.git
   cd test-automation-framework
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Configure environment:**
   ```bash
   cp config/dev.env .env
   ```

---

##  Running Tests

### Run all tests
```bash
pytest tests/
```

### Run UI tests only
```bash
pytest tests/ui/
```

### Run API tests only
```bash
pytest tests/api/
```

### Run with detailed logging
```bash
pytest tests/ -v --log-cli-level=DEBUG
```

### Run with HTML report
```bash
pytest tests/ --html=reports/index.html --self-contained-html
```

### Run specific test class
```bash
pytest tests/ui/test_authentication.py::TestAuthentication
```

### Run tests in parallel
```bash
pytest tests/ -n 4
```

---

##  Core Components

### 1. Logger Configuration

The framework includes a custom logger for detailed test execution logging:

```python
# core/logger.py
from core.logger import get_logger

logger = get_logger(__name__)
logger.info("Test started")
logger.debug("Debug information")
logger.error("Error occurred")
```

### 2. Base Test Class

All tests inherit from the base test class for common functionality:

```python
# core/base_test.py
from core.base_test import BaseTest

class TestAuthentication(BaseTest):
    def test_login(self):
        logger = self.logger
        logger.info("Testing login functionality")
```

### 3. Custom Assertions

The framework provides custom assertions for better readability:

```python
# core/assertions.py
from core.assertions import assert_status_code, assert_element_visible

assert_status_code(response, 200)
assert_element_visible(page, selector)
```

### 4. Base Page Object

All page objects inherit from the base page for common methods:

```python
# ui/base_page.py
from ui.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
```

### 5. Base API Client

All API clients inherit from the base client:

```python
# api/base_api_client.py
from api.base_api_client import BaseAPIClient

class UserAPI(BaseAPIClient):
    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")
```

---

##  Test Reporting

The framework generates comprehensive HTML reports:

```bash
pytest tests/ --html=reports/index.html --self-contained-html
```

Reports include:
- Test execution summary
- Pass/fail status for each test
- Execution time
- Error details and screenshots
- Test history

---

##  Configuration Management

The framework supports multiple environments:

```python
# config/config.py
from config import get_config

config = get_config(env="dev")
base_url = config.BASE_URL
timeout = config.TIMEOUT
```

---

##  Example Tests

### UI Test Example

```python
# tests/ui/test_authentication.py
from core.base_test import BaseTest
from ui.pages.login_page import LoginPage

class TestAuthentication(BaseTest):
    def test_valid_login(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("user@example.com", "password123")
        assert page.url.endswith("/dashboard")
```

### API Test Example

```python
# tests/api/test_users_api.py
from core.base_test import BaseTest
from api.endpoints.user_api import UserAPI

class TestUsersAPI(BaseTest):
    def test_get_user(self):
        api = UserAPI()
        response = api.get_user(1)
        assert response.status_code == 200
```

---

##  Key Learnings

This framework demonstrates:
1. **Layered Architecture:** Separation of concerns (UI, API, Utils)
2. **Reusable Components:** Base classes and utilities for DRY code
3. **Professional Logging:** Detailed logs for debugging
4. **Configuration Management:** Environment-specific settings
5. **Advanced Reporting:** Comprehensive test reports
6. **Best Practices:** Industry-standard patterns and conventions

---

##  Related Repositories

- [qa-portfolio-overview](https://github.com/Ayoub-DataScientist/qa-portfolio-overview) - Portfolio overview
- [web-ui-testing-playwright](https://github.com/Ayoub-DataScientist/web-ui-testing-playwright) - UI testing
- [api-testing-automation](https://github.com/Ayoub-DataScientist/api-testing-automation) - API testing
- [qa-ci-cd-examples](https://github.com/Ayoub-DataScientist/qa-ci-cd-examples) - CI/CD workflows

---

##  License

This project is open source and available under the MIT License.
