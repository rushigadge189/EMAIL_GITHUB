import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Logs.test_logger import Test_LogGenerator


class Test_Oranghrm_log() :

    log=Test_LogGenerator.logger() ;

    def test_loghrm(self):
        driver = webdriver.Chrome() ;
        self.log.info("Open The Browser");

        driver.implicitly_wait(2) ;

        driver.maximize_window();
        self.log.info("Maximize The Browser") ;

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        self.log.info("Go to The OrnageHRM Login Page") ;

        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin') ;
        self.log.info("Enter Username") ;

        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin123') ;
        self.log.info("Eneter Browser") ;

        driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;
        self.log.info("Click On Login Button") ;

        driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click();

        driver.find_element(By.XPATH, "//a[text()='Logout']").click() ;
        self.log.info("Loout Form The Application") ;

        try:
            driver.find_element(By.XPATH, '//img[@alt="company-branding"]') ;
            print('LOGIN-LOGOUT SUCCESSFUL') ;
            assert True

        except NoSuchElementException :
            print('LOGIN_LOGOUT UNSUCCESSFUL') ;
            assert False

        self.log.debug("THIS IS DEBUG");
        self.log.warning("THIS IS WARNING") ;
        self.log.critical("THIS IS CRITICAL");
        self.log.error("THIS IS ERROR");
        self.log.critical("THIS IS CRITICAL");



        driver.close() ;