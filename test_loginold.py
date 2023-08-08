import time


from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_loginold() :

    def test_login_old(self):
        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.get("https://trytestingthis.netlify.app/") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="uname"]').send_keys('test') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="pwd"]').send_keys('test') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@value="Login"]').click();
        time.sleep(1) ;

        driver.find_element(By.XPATH, "//a[text()='here']").click();
        time.sleep(1) ;

        driver.close();