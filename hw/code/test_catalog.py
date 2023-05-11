from ui.components.catalog_components import CatalogComponent
from ui.locators.base_locators import BaseLocators
from ui.locators.catalog_locators import CatalogLocators

import pytest


# @pytest.mark.skip('skip')
class TestCategorySelection():
    baseLocators = BaseLocators()

    search = CatalogComponent(
        CatalogLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.search
        + '?q=iphone')

    category = CatalogComponent(
        CatalogLocators,
        baseLocators.hrefs.domain + baseLocators.hrefs.category
        + baseLocators.hrefs.phones)

    def test_category_search_favourites(self):
        self.search.checkSort()
        self.search.checkTab()
        self.search.checkIfPhotoBroken()

    def test_category_category_favourites(self):
        self.category.checkSort()
        self.category.checkTab()
        self.category.checkIfPhotoBroken()
