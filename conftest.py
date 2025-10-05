import pytest
from selenium import webdriver
from urls import MAIN_PAGE_URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()