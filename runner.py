import os
from time import sleep

import pytest

from PageObject.base_page import get_cookies

# os.popen("chrome --remote-debugging-port=9222")
# sleep(2)
# get_cookies()
pytest.main(['-s', '-v'])

