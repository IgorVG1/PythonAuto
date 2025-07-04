from webbrowser import open_new

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Preconditions :
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()

# Test 1 :
def test_1(driver):
    open_page1 = driver.get('https://www.wildberries.ru/')
    search_box = driver.find_element(By.CSS_SELECTOR, 'input[id="searchInput"]').send_keys('pwr ultimate power bcaa' + Keys.ENTER)
    ticket_page = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.wildberries.ru/catalog/268269380/detail.aspx"]').click()
    send_in_basket = driver.find_element(By.XPATH,'(//div[@class="order__buttons"])[2]').click()
    open_basket = driver.find_element(By.XPATH, "(//a[text()='Перейти в корзину'])[2]").click()
    assert driver.find_element(By.XPATH, '//span[text()="BCAA порошок 2-1-1 500гр"]').is_displayed()

# Test 2 :
def test_2(driver):
    open_page2 = driver.get('https://gunnars.ru/')
    open_page_glasses = driver.find_element(By.XPATH, '(//div[@class="category_row-item category_row-item-youth"])[1]').click()
    waiting = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//a[@class="gunnar-open-vto"])[3]')))
    amount_glasses = driver.find_elements(By.XPATH,'//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')
    assert len(amount_glasses) == 3