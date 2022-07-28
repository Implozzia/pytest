import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomePage:
    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.find_element(By.CSS_SELECTOR, '#1')

        wait = WebDriverWait(driver, 15)
        element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id')))