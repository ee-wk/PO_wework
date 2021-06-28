from typing import List

import pytest

from PageObject.main_page import MainPage


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print("items ===>", items)
    for item in items:
        # item.name 测试用例的名字
        # item.nodeid 测试用例的路径
        # print(item.name)
        # print(item.nodeid)
        # 修改测试用例的编码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# @pytest.fixture
# def duplicate_data():
#     main = MainPage()
#     main.click_contact().click_add_department().edit_content("客服一部")

@pytest.fixture(scope='class')
def logging():
    logging.info("开始执行")
    yield
    logging.info("结束执行")
