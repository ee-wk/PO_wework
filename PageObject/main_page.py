from selenium.webdriver.common.by import By

from PageObject.base_page import BasePage
from PageObject.contact_page import ContactPage


class MainPage(BasePage):
    # 定位器
    _contact_button = (By.XPATH, '//*[@id="menu_contacts"]/span')

    def click_contact(self):
        """点击通讯录，返回通讯录页面"""
        self.find_element(*self._contact_button).click()
        return ContactPage(self.driver)
