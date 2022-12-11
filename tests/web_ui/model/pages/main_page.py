from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class MainPage:

	@step
	def fill_input(self, value):
		browser.element(by.xpath('nav [type="search"]'))\
			.type(value).press_enter()
		return self

	@step
	def check_query_results(self, value):
		browser.element(by.xpath('[data-widget="fulltextResultsHeader"]'))
