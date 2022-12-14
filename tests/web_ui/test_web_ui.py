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

from tests.web_ui.application_manager import app


search_value = 'PlayStation 5'
first_subcategory = "ПК, ноутбуки, периферия"
second_subcategory = "Ноутбуки и аксессуары"
third_subcategory = "Ноутбуки"
product_value = "Apple iPhone 14 Pro Max 256 ГБ фиолетовый"




@pytest.mark.web
@allure.description('TEST: Open user profile')
def test_open_user_profile(open_main_page):
	"""
	TEST: Open user profile
	"""
	app.main_page\
		.move_to_element_enter()\
		.should_be_user_profile_present()


@pytest.mark.web
@allure.description('TEST: Open entry form')
def test_open_entry_form(open_main_page):
	"""
	TEST: Open entry form
	"""
	app.main_page.\
		move_to_element_enter().\
		click_on_enter_button().\
		should_be_entry_form_present()


@pytest.mark.web
@allure.description('TEST: Query results')
def test_search_results(open_main_page):
	"""
	TEST: Query results
	"""
	app.main_page.\
		fill_search_input(search_value)
	app.catalog_page.should_be_correct_results(search_value)


@pytest.mark.web
@allure.description('TEST: Go to subcategory')
def test_open_subcategory_desktop(open_main_page):
	"""
	TEST: Go to subcategory
	"""
	app.main_page.\
		click_on_first_subcategory(first_subcategory).\
		should_be_correct_first_category_title(first_subcategory)


@pytest.mark.web
@allure.description('TEST: Open laptop list')
def test_open_laptop_list(open_main_page):
	"""
	TEST: Open laptop list
	"""
	app.main_page.\
		click_on_first_subcategory(first_subcategory)
	app.catalog_page.\
		click_on_subcategory(second_subcategory).\
		should_be_correct_subcategory_title(second_subcategory).\
		click_on_subcategory(third_subcategory). \
		should_be_correct_title(third_subcategory)


@pytest.mark.web
@allure.description(f'TEST: Open product {product_value} page')
def test_open_product_page(open_main_page):
	"""
	TEST: Open product page
	"""
	app.main_page.\
		fill_search_input(product_value)
	app.catalog_page.\
		should_be_correct_results(product_value).\
		click_on_product_name(product_value)
	app.product_page.\
		should_be_product_title_is_present(product_value)


@pytest.mark.web
@allure.description(f'TEST: Add product {product_value} to wishlist')
def test_add_product_to_wishlist(open_main_page):
	"""
	TEST: Add to wishlist
	"""
	app.main_page.\
		fill_search_input(product_value)
	app.catalog_page.\
		click_on_product_name(product_value)
	app.product_page.\
		click_on_add_to_wishlist_button(). \
		should_be_wishlist_button_is_done().\
		should_be_wishlist_bange_is_one()





