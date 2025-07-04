import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 0 - Precondition :
@pytest.fixture()
def browser():
# Open browser
    browser = webdriver.Firefox()
# Take fullscreen
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()

# Test 1 - Feedback page
def test_1_open_page(browser):
    browser.get('https://www.bspb.ru')
    browser.find_element(By.XPATH, '//h3[@class="css-2wq498"][text()="Вклады"]').click()
    browser.find_element(By.XPATH, '//button[text()="Вклады"]').click()
    assert browser.find_element(By.XPATH, '//button[text()="Вклады"][@tabindex="0"]').is_displayed()

# Test 2 -