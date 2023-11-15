import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    #Creating an object to control the browser
    driver = webdriver.Chrome(
        service=Service(f'c:/Users/Alex/QAcourse/' + 'chromedriver.exe')
        )

    #open the page https://github.com/login
    driver.get ("https://github.com/login")

    #We find the field in which we will enter the wrong username or postal address
    login_element = driver.find_element(By.ID, "login_field")

    #Enter an incorrect username or email address
    login_element.send_keys("kleunodlav@mistakeinemail.com")
    
    #We find the field in which we will enter the wrong password
    pass_elem = driver.find_element(By.ID, "password")

    #Enter the wrong password
    pass_elem.send_keys("wrong password")

    #We find the button sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    #Emulate a click with the left mouse button
    btn_elem.click()

    #We check that the name of the page is what we expect 
    assert driver.title == "Sign in to GitHub · GitHub"

    #Close the browser
    driver.close()