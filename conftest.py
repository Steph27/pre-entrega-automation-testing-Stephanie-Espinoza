import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return{"x-api-key": "reqres_ae8f7a31c74e4df8a2e8c1cf4b12f98a"}
