import time

from selenium import webdriver ;
import pytest

@pytest.fixture()
def setup() :
    driver=webdriver.Chrome();
    time.sleep(1);

    driver.maximize_window();
    time.sleep(1);

    return driver ;