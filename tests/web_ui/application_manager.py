from tests.web_ui.pages.catalog_page import CatalogPage
from tests.web_ui.pages.main_page import MainPage
from tests.web_ui.pages.product_page import ProductPage


class ApplicationManager():
    def __init__(self):
        self.main_page = MainPage()
        self.catalog_page = CatalogPage()
        self.product_page = ProductPage()


app = ApplicationManager()