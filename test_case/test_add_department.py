import logging

import allure
import pytest
import yaml

from PageObject.main_page import MainPage


def get_data():
    with open("./data/dep_name.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


@allure.feature("添加部门")
class TestAddDepartment:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close()

    @allure.story("添加部门的正常场景")
    @pytest.mark.parametrize("dep_name,title", get_data()["level_one"]["data"], ids=get_data()["level_one"]["ids"])
    def test_add_department(self, dep_name, title):
        """正常情况"""
        allure.title(title)
        logging.info(f"执行用例{title}")
        dep_list = self.main.click_contact().click_add_department().edit_content(dep_name).get_department()
        print(dep_list)
        assert dep_name in dep_list  # 断言新添加的部门在部门列表里

    @allure.story("添加部门的异常场景")
    @pytest.mark.parametrize("dep_name,expect_tips,title", get_data()["abnormal"]["data"],
                             ids=get_data()["abnormal"]["ids"])
    def test_add_department_abnormal(self, dep_name, expect_tips, title):
        """异常情况"""
        allure.title(title)
        logging.info(f"执行用例{title}")
        tips = self.main.click_contact().click_add_department().edit_content(dep_name).get_tips()  # 执行操作并获取提示信息
        assert expect_tips == tips  # 断言提示与预期一致
