from allure_commons._allure import step
from selene import by, have, be
from selene.support import webdriver
from selene.support.shared import browser
from selenium.webdriver import ActionChains


class CatalogPage:

    @step
    def should_be_correct_results(self, value):
        browser.element('[class="catalog-product__name ui-link ui-link_black"]').should(have.text(value))
        return self

    @step
    def click_on_subcategory(self, value):
        browser.all('[class="subcategory__title"]').element_by(have.text(value)).click()
        return self

    @step
    def should_be_correct_subcategory_title(self, value):
        browser.element('[class="subcategory__page-title"]').should(have.text(value))
        return self

    @step
    def should_be_correct_title(self, value):
        browser.element('[class="title"]').should(have.text(value))
        return self

    @step
    def click_on_wishlist_button(self):
        wishlist_button = browser.all('//button[contains(@class, "button-ui")]')[5]
        wishlist_button.click()
        return self

    @step
    def should_be_wishlist_button_is_done(self):
        browser.element('//button[contains(@class, "button-ui_done")]').should(be.visible)
        return self

    @step
    def should_be_wishlist_modal_is_presend(self):
        browser.element('.wishlist-login-modal__modal-content').should(be.visible)
        return self

    @step
    def close_wishlist_modal_window(self):
        browser.element('.ui-link ui-link_gray_dark').should(be.present).click()
        return self

    @step
    def click_on_product_name(self, value):
        browser.element('.catalog-product__name').should(have.text(value)).click()
        return self
