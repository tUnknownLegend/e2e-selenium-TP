from ui.components.catalog_selector import CatalogSelectorComponent
from ui.locators.header_locators import HeaderLocators
from ui.locators.home_locators import HomeLocators
import pytest


class TestCategorySelection():
    headerSelector = CatalogSelectorComponent(HeaderLocators)
    homeSelector = CatalogSelectorComponent(HomeLocators)

    @pytest.mark.skip('skip')
    def test_header_category_select(self):
        self.headerSelector.test_is_header_catalog_links()

    def test_home_category_select(self):
        self.homeSelector.test_is_home_catalog_links()
