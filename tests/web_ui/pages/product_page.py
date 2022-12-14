from allure_commons._allure import step
from selene import by, have, be
from selene.support import webdriver
from selene.support.shared import browser
from selenium.webdriver import ActionChains


class ProductPage:

    @step
    def should_be_product_title_is_present(self, value):
        browser.element('.product-card-top__title').should(have.text(value))
        return self

    @step
    def click_on_add_to_wishlist_button(self):
        browser.element('.wishlist-btn').should(be.clickable).click()
        return self

    @step
    def should_be_wishlist_button_is_done(self):
        browser.element('//button[contains(@class, "button-ui_done")]').should(be.visible)
        return self

    @step
    def should_be_wishlist_bange_is_one(self):
        browser.element('.wishlist-link__badge').should(have.text('1'))
        return self