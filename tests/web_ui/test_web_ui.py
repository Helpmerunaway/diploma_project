"""

Web UI tests for DNS shop

"""
import time

from selene.support.conditions import be, have
from selene.support.shared import browser
import allure
import pytest
import selene
from selenium.webdriver import ActionChains


@pytest.mark.web
@allure.description('Test open auth form')
def test_open_auth_form(open_main_page):
	"""
	test open auth form modal window
	:return:
	"""
	with allure.step('Клик на кнопку "Войти"'):
		browser.element('[class="user-profile__login-icon"]').click()
	with allure.step('Форма Входа в Личный Кабинет присутствует на странице'):
		browser.element('[class="user-profile__guest-text"]')\
			.should(have.text('Получайте бонусы, сохраняйте и отслеживайте заказы.'))


@pytest.mark.web
@allure.description('Test search is working')
def test_search_functionality(open_main_page):
	"""
	test search func
	:return:
	"""
	with allure.step('Клик на поле поиск'):
		search_input = browser.element('nav [type="search"]')
		search_input.click()
	with allure.step('Заполняем поле поиск'):
		search_input.send_keys('playstation 5').press_enter()
	with allure.step('В результатах поиска присутствует текст запроса'):
		browser.element('[class="products-list__content"]')\
			.should(have.text('PlayStation 5'))


@pytest.mark.web
@allure.description('Test go to subcategory page desktop')
def test_open_subcategory_desktop(open_main_page):
	"""
	test open_shops_moscow
	:param open_main_page:
	:return:
	"""
	with allure.step('Клик на кнопку "ПК, ноутбуки, периферия"'):
		desktop_button = browser.all('[class="ui-link menu-desktop__root-title"]')[4]
		desktop_button.click()
	with allure.step('Открыта страница ПК, нотбуки, периферия'):
		browser.element('[class="subcategory__page-title"]')\
			.should(have.text('ПК, ноутбуки, периферия'))


@pytest.mark.web
@allure.description('Test add to wishlist')
def test_add_to_wishlist(open_main_page):
	"""

	:param open_main_page:
	:return:
	"""
	with allure.step('Клик на Смартфоны'):
		browser.element('[class="homepage-brands__item tns-item tns-slide-active"]').click()
		time.sleep(5)
		browser.element('[class="button-ui button-ui_white button-ui_icon wishlist-btn"]').click()
		time.sleep(5)
		browser.element('[class="wishlist-link__lbl"]').click()






