from time import sleep

from PageObject.add_department_page import AddDepartmentPage
from PageObject.base_page import BasePage


class ContactPage(BasePage):

    def click_add_department(self):
        self.driver.find_element_by_xpath('//*[@id="main"]//div/div[1]/div/div[1]/a/i').click()  # 点击“+”
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul/li[1]/a').click()   # 选择添加部门
        '//*[@id="js_contacts86"]/div/div[1]/ul/li[1]/a'
        return AddDepartmentPage(self.driver)

    def get_department(self):
        sleep(1)
        dep_elem = self.driver.find_elements_by_xpath('//*[@id="1688852052171016"]/ul/li/a')
        dep_name = []
        for ele in dep_elem:
            dep_name.append(ele.text)
        return dep_name
