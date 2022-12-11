import os
import pytest
from selene.support.conditions import have
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# from ui.helpers import attach

#BASE_URL = 'https://www.computeruniverse.net/ru'
BASE_URL = 'https://www.dns-shop.ru/'


@pytest.fixture(scope='function', autouse=True)
def browser_managemento():
    print('Starting browser')
    browser.config.wait_for_no_overlap_found_by_js = True
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 4
    browser.config.window_width = 1700
    browser.config.window_height = 1200


@pytest.fixture()
def open_main_page():
    browser.open(BASE_URL)
    browser.should(have.title('DNS – интернет магазин цифровой и бытовой техники по доступным ценам.'))
    #browser.element('[class="main-header"]').should(have.text('Practice Form'))