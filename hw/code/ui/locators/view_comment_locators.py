from selenium.webdriver.common.by import By
from ui.hrefs import Hrefs


class ViewCommentLocators():
    def __init__(self):
        self.hrefs = Hrefs()

    ADD_COMMENT_BUTTON = (
        By.ID, 'add-comment-btn'
    )
