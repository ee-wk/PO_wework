from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage, wait_clickable


class AddDepartmentPage(BasePage):
    _dep_name_input_box = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input')
    _dep_list_button = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a')
    _choose_dep_button = (By.XPATH, '//*[@id="__dialog__MNDialog__"]//div/ul/li/a')
    _ok_button = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

    def edit_content(self):
        from PageObject.contact_page import ContactPage
        self.find_element(*self._dep_name_input_box).send_keys("客服一部")
        self.find_and_click(*self._dep_list_button)
        wait_clickable(self.driver, *self._choose_dep_button)
        self.find_and_click(*self._choose_dep_button)
        self.find_and_click(*self._ok_button)
        return ContactPage(self.driver)
