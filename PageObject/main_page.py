from selenium.webdriver.common.by import By

from PageObject.base_page import BasePage
from PageObject.contact_page import ContactPage


class MainPage(BasePage):
    _contact_button = (By.XPATH, '//*[@id="menu_contacts"]/span')

    def click_contact(self):
        self.find_element(*self._contact_button).click()
        return ContactPage(self.driver)
