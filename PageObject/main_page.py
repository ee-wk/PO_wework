from PageObject.base_page import BasePage
from PageObject.contact_page import ContactPage


class MainPage(BasePage):

    def click_contact(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        return ContactPage(self.driver)
