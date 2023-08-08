import time

from selenium import webdriver ;
from test_email_page import Test_Email

class Test_Email_Prg() :

    def test_email_notification(self,setup):
        self.driver=setup ;

        self.obj=Test_Email(self.driver) ;#calling A Constructor

        self.obj.test_open_page('https://practice.expandtesting.com/login');

        self.obj.test_enter_username('practice') ;

        self.obj.test_enter_password('SuperSecretPassword!') ;

        self.obj.test_login_button();

        self.obj.test_logout();

        try :
            if(self.driver.title== "Test Automation Practice: Working with Login form"):
                print('LIGIN-LOGOUT SUCCESSFUL') ;
                assert True;
        except:
            if (self.driver.title != "Test Automation Practice: Working with Login form"):
                print('LIGIN-LOGOUT UNSUCCESSFUL');
                assert False;

        self.driver.close();



