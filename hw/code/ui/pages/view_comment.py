from ui.pages.base_page import BasePage
from ui.locators.view_comment_locators import ViewCommentLocators
import time


class ViewComment(BasePage):

    def __init__(self, driver):
        super(ViewComment, self).__init__(driver)
        self.locators = ViewCommentLocators()
        self.url = self.locators.hrefs.domain + self.locators.hrefs.comment + '/43'

    def checkErrorAddComment(self):
        self.getAddCommentButton().click()

        self.checkErrorMessage('Вы уже создали отзыв об этом товаре')

    def getAddCommentButton(self):
        self.waitUntilVisible(self.locators.ADD_COMMENT_BUTTON, 1)
        return self.find(self.locators.ADD_COMMENT_BUTTON)

    def checkUnauthAddComment(self):
        id = self.driver.current_url.split('/')[-1]

        time.sleep(5)

        self.getAddCommentButton().click()

        time.sleep(5)

        self.is_opened(self.locators.hrefs.domain +
                       self.locators.hrefs.addComment + '/' + id
                       )
