import pytest
from PageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import excelUtil


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()

    @pytest.mark.parametrize("username,password", excelUtil.get_data("TestData/testdata.xlsx", "logintestsheet"))
    def test_valid_credentials(self, setup, username, password):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.insert_username(username)
        self.lp.insert_password(password)
        self.lp.click_login_button()
        self.lp.verify_edit_link()
