import time
from selenium import webdriver
from pomdemo.tests.pages.test_login_page import Test_Login_Page

class Test_login_new() :

    def test_login_new(self,setup):
        self.driver=setup ;

        self.lpobj=Test_Login_Page(self.driver) ;
        time.sleep(1) ;

        self.lpobj.test_open_page("https://trytestingthis.netlify.app/") ;
        time.sleep(1) ;

        self.lpobj.test_enter_username("test") ;
        time.sleep(1) ;

        self.lpobj.test_enter_password("test") ;
        time.sleep(1)

        self.lpobj.test_click_login() ;
        time.sleep(1)

        self.lpobj.test_logout() ;
        time.sleep(1) ;


        self.driver.close();

        
