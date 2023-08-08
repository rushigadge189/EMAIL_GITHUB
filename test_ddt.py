import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtils

class Test_ddt() :

    def test_ddt_001(self):
        driver= webdriver.Chrome() ;

        driver.implicitly_wait(10) ;

        driver.maximize_window() ;

        driver.get('https://practicetestautomation.com/practice-test-login/') ;

        path = "D:\PYTHON CT15\AUTOMATION_PROJECTS\Login1.xlsx" ;

        rows=XLUtils.getRowCount(path, 'Sheet1') ;

        for r in range(2, rows+1) :
            username=XLUtils.readData(path, 'Sheet1', r, 1) ;
            password=XLUtils.readData(path,'Sheet1', r, 2) ;

            driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(username) ;

            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password) ;

            driver.find_element(By.XPATH, "//button[text()='Submit']").click() ;


            if (driver.title == "Logged In Successfully | Practice Test Automation") :
                print ( 'TEST IS PASSED' ) ;
                XLUtils.writeData(path, 'Sheet1', r, 3, "Passed") ;
            else:
                print ('TEST IS FAILED') ;
                XLUtils.writeData(path, 'Sheet1', r, 3, "Failed") ;

            driver.get('https://practicetestautomation.com/practice-test-login/') ;


