from allure_commons._allure import step
from selene import by, have, be
from selene.support import webdriver
from selene.support.shared import browser
from selenium.webdriver import ActionChains


class MainPage:

	@step
	def fill_search_input(self, value):
		browser.element('nav [type="search"]')\
			.type(value).press_enter()
		return self



	@step
	def move_to_element_enter(self):
		user_profile = browser.element('[class="user-profile__login-icon"]')
		ActionChains(browser.driver).move_to_element_with_offset(user_profile.should(be.visible)(), 5, 5).perform()

		return self

	@step
	def click_on_enter_button(self):
		browser.all('.base-ui-button-v2__text').element_by(have.text('Войти')).click()
		return self

	@step
	def should_be_entry_form_present(self):
		browser.element('.form-entry-or-registry').should(be.visible)
		return self

	@step
	def should_be_user_profile_present(self):
		browser.element('.user-profile__menu').should(be.visible)
		browser.element('[class="user-profile__guest-text"]') \
			.should(have.text('Получайте бонусы, сохраняйте и отслеживайте заказы.'))
		return self

	@step
	def click_on_first_subcategory(self, value):
		browser.all('[class="ui-link menu-desktop__root-title"]')\
			.element_by(have.text(value)).click()
		return self

	@step
	def should_be_correct_first_category_title(self, value):
		browser.element('[class="subcategory__page-title"]').should(have.text(value))
		return self


