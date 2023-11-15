from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #We find the field in which we will enter the wrong username or postal address
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Enter an incorrect username or email address
        login_elem.send_keys(username)

        #We find the field in which we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        #Enter the wrong password
        pass_elem.send_keys(password)

        #We find the sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        #Emulate a click with the left mouse button 
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title  