from ui.components.changeCartCountButton import ChangeCartCountButton
from ui.locators.cart_count_locators import CartCountLocators
from ui.locators.horizontal_scroll_catalog_locators import HorizontalScrollCatalogLocators

# import pytest


# @pytest.mark.skip('skip')
class TestChangeItemCountInCart():
    productChangeCount = ChangeCartCountButton(CartCountLocators)
    recommendationsItemChangeCount = ChangeCartCountButton(
        HorizontalScrollCatalogLocators)

    def test_product_change_count(self):
        self.productChangeCount.test_unauth_change_count_buttons()
        self.productChangeCount.test_auth_change_count_buttons()

    def test_recommendation_change_count(self):
        self.recommendationsItemChangeCount.test_unauth_change_count_buttons()
