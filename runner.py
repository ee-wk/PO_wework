# -*- coding: utf-8 -*-
import os
import shutil
import pytest
import time
from PageObject.base_page import get_cookies

now = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取实时时间
file_name = f'report_{now}'


def runner(tag=False):
    if tag:
        os.popen("chrome --remote-debugging-port=9222")
        time.sleep(2)
        get_cookies()
    pytest.main(['-vs',  '--alluredir', './temp'])
    os.system(f'allure generate ./temp -o ./report/{file_name} --clean')
    f = os.getcwd()
    path = f + '\\temp'
    shutil.rmtree(path)


if __name__ == '__main__':
    runner()
