from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_Login_Page() :

    def __init__(self,driver) :
        self.driver=driver ;
        self.username_textbox=(By.XPATH, '//input[@id="uname"]') ;
        self.password_textbox=( By.XPATH, '//input[@id="pwd"]') ;
        self.login_button=(By.XPATH, '//input[@type="submit"]') ;
        self.logout_link=(By.XPATH, "//a[text()='here']") ;

    def test_open_page(self,url):
        self.driver.get(url);

    def test_enter_username (self,username) :
        self.driver.find_element(*self.username_textbox).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password) ;

    def test_click_login(self):
        self.driver.find_element(*self.login_button).click() ;

    def test_logout(self):
        self.driver.find_element(*self.logout_link).click() ;
