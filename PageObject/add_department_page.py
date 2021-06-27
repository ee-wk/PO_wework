from time import sleep

from PageObject.base_page import BasePage


class AddDepartmentPage(BasePage):

    def edit_content(self):
        from PageObject.contact_page import ContactPage
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("客服一部")
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]//div/ul/li/a').click()
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return ContactPage(self.driver)
