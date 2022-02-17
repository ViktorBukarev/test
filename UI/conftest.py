import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#Указываем предварительные настройки




@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()