import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            with open("./data/cookies.yaml", encoding="utf-8") as f:
                cookies = yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = base_driver

    def close(self):
        self.driver.close()


def get_cookies():
    """获取cookies"""
    option = Options()
    option.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    expect = expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="menu_contacts"]/span'))
    WebDriverWait(driver, 30).until(expect)
    cookies = driver.get_cookies()
    with open("./data/cookies.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(cookies, f)


def debugging():
    option = Options()
    option.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=option)
    dep_list = driver.find_elements_by_xpath('//*[@id="1688852052171016"]/ul/li/a')
    for i in dep_list:
        print(i.text)
    print(dep_list)


if __name__ == '__main__':
    debugging()
