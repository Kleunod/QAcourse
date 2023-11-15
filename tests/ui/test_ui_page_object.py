from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    #creating a page object
    sign_in_page = SignInPage()

    #open the page https://github.com/login 
    sign_in_page.go_to()

    #we try to log in to the GitHub system
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #We check that the name of the page is what we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    #Close the browser
    sign_in_page.close()
