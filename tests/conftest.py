import os
import time
from selene import command, be
from selene.support.conditions import have
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# from ui.helpers import attach

BASE_URL = 'https://www.dns-shop.ru/'


# обертка над библиотекой requests
import allure
import pytest
import requests


class ApiClient:
	def __init__(self, base_address):
		self.base_address = base_address

	# аргументы функции path, params, headers передаются в гет
	def get(self, path="/", params=None, headers=None):
		url = f"{self.base_address}{path}"
		with allure.step(f"GET request to: {url}"):
			return requests.get(url=url, params=params, headers=headers)

	def post(self, path='/', params=None, data=None, json=None, headers=None):
		url = f"{self.base_address}{path}"
		with allure.step(f"POST request to: {url}"):
			return requests.post(url=url, params=params, data=data, json=json, headers=headers)


@pytest.fixture
def dog_api():
	return ApiClient(base_address='https://dog.ceo/api/')


@pytest.fixture(scope='session', autouse=True)
def auto_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_managemento():
    print('Starting browser')
    browser.config.wait_for_no_overlap_found_by_js = True
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = False
    browser.config.timeout = 6
    browser.config.window_width = 1600
    browser.config.window_height = 900


@pytest.fixture()
def open_main_page():
    browser.open(BASE_URL)
    browser.should(have.title('DNS – интернет магазин цифровой и бытовой техники по доступным ценам.'))