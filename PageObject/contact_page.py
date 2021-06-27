from selenium.webdriver.common.by import By
from PageObject.add_department_page import AddDepartmentPage
from PageObject.base_page import BasePage, wait_clickable


class ContactPage(BasePage):
    _add_list_button = (By.XPATH, '//*[@id="main"]//div/div[1]/div/div[1]/a/i')
    _add_dep_button = (By.XPATH, '//*[@id="main"]/div/div/div[1]/ul/li[1]/a')
    _dep_list = (By.XPATH, '//*[@id="1688852052171016"]/ul/li/a')

    def click_add_department(self):
        self.find_and_click(*self._add_list_button)  # 点击“+”
        self.find_and_click(*self._add_dep_button)  # 选择添加部门
        return AddDepartmentPage(self.driver)

    def get_department(self):
        wait_clickable(self.driver, By.XPATH, '//*[@id="main"]//div[2]/div[2]/div[1]/div[2]')
        dep_elem = self.find_elements(*self._dep_list)
        dep_name = []
        for ele in dep_elem:
            dep_name.append(ele.text)
        return dep_name
