from ui.components.changeCartCountButton import ChangeCartCountButton
from ui.locators.cart_count_locators import CartCountLocators
from ui.locators.horizontal_scroll_catalog_locators import HorizontalScrollCatalogLocators
from ui.locators.base_locators import BaseLocators
from ui.locators.comment_titile_locators import CommentTitleLocators
from ui.locators.home_locators import HomeLocators

# import pytest


# @pytest.mark.skip('skip')
class TestChangeItemCountInCart():

    baseLocator = BaseLocators()

    productChangeCount = ChangeCartCountButton(
        CartCountLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.product + '/43')

    viewComment = ChangeCartCountButton(
        CommentTitleLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.comment + '/43')

    addComment = ChangeCartCountButton(
        CommentTitleLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.addComment + '/43')

    homePage = ChangeCartCountButton(
        HomeLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.home)

    recommendationsItemChangeCount = ChangeCartCountButton(
        HorizontalScrollCatalogLocators,
        baseLocator.hrefs.domain + baseLocator.hrefs.product + '/43')

    def test_product_change_count(self):
        self.productChangeCount.test_unauth_change_count_buttons()
        self.productChangeCount.test_auth_change_count_buttons()

    def test_product_view_comment_change_count(self):
        self.viewComment.test_unauth_change_count_buttons()
        self.viewComment.test_auth_change_count_buttons()

    def test_product_add_comment_change_count(self):
        self.addComment.test_auth_change_count_buttons()

    def test_home_page_change_count(self):
        self.homePage.test_unauth_change_count_buttons()
        self.homePage.test_auth_change_count_buttons()

    def test_recommendation_change_count(self):
        self.recommendationsItemChangeCount.test_unauth_change_count_buttons()
