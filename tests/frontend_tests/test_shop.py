import pytest
from selenium.webdriver.common.by import By

url = "https://testqastudio.me/"

def test_product_view_sku(browser):
    
    # определяем адрес страницы для теста и переходим на неё
    browser.get(url=url) 

		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()

		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    element = browser.find_element(by=By.XPATH, value='//*[@id="rz-shop-content"]/ul/li[5]')
    element.click()

		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")

		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"