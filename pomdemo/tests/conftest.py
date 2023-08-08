import time

import pytest
from selenium import webdriver

@pytest.fixture
def setup() :
    driver = webdriver.Chrome();
    time.sleep(1);

    driver.maximize_window();
    time.sleep(1);

    return driver