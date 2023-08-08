import time
from selenium.webdriver.common.by import By


class Test_Email() :

    def __init__(self,driver):
        self.driver=driver ;
        self.username_textbox=(By.XPATH, '//input[@id="username"]') ;
        self.password_textbox=(By.XPATH, '//input[@id="password"]') ;
        self.login_button=(By.XPATH, '//button[text()="Login"]') ;
        self.logout_link=(By.XPATH, '//i[text()=" Logout"]');

    def test_open_page(self,url):
        self.driver.get(url) ;
        time.sleep(1) ;

    def test_enter_username(self,username):
        self.driver.find_element(*self.username_textbox).send_keys(username);
        time.sleep(1);

    def test_enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password) ;
        time.sleep(1) ;

    def test_login_button(self) :
        self.driver.find_element(*self.login_button).click();
        time.sleep(1) ;

    def test_logout(self) :
        self.driver.find_element(*self.logout_link).click();
        time.sleep(1) ;