import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()