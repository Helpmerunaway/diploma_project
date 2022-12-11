from tests.web_ui.pages.catalog_page import CatalogPage
from tests.web_ui.pages.main_page import MainPage


class ApplicationManager():
    def __init__(self):
        self.main_page = MainPage()
        self.catalog_page = CatalogPage()



app = ApplicationManager()