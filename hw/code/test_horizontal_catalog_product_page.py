import allure
import pytest
import time

from ui.fixtures import get_driver
from ui.pages.horizontal_scroll_catalog_locators import HorizontalScrollCatalog


# @pytest.mark.skip('skip')
class TestHorizontalScroll():
    driver = get_driver(browser_name='chrome')
    horizontalScroll = HorizontalScrollCatalog(driver)

    @allure.feature('Test product recommendations')
    @allure.story('scroll')
    @horizontalScroll.render_decorator
    def test_scroll_buttons(self):
        with allure.step('scroll to the container'):
            self.horizontalScroll.scrollToTheContainer()

        with allure.step('checkItemsVisibleLeft initial'):
            self.horizontalScroll.checkScrollShiftLeft()

        with allure.step('scrollRight'):
            self.horizontalScroll.scrollRight()

        time.sleep(3)

        with allure.step('checkItemsVisibleRight'):
            self.horizontalScroll.checkScrollShiftRight()

        with allure.step('scrollLeft'):
            self.horizontalScroll.scrollLeft()

        time.sleep(3)

        with allure.step('checkItemsVisibleLeft after scroll back and forth'):
            self.horizontalScroll.checkScrollShiftLeft()

    @allure.feature('Test product recommendations')
    @allure.story('title link')
    def test_title_link(self):
        self.horizontalScroll.checkTitleLink()

    @allure.feature('Check photo')
    @allure.story('is photo broken')
    def test_photo_broken(self):
        self.horizontalScroll.scrollToTheContainer()
        self.horizontalScroll.checkPhotoBroken()