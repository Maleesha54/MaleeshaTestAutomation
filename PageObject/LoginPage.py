from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    INSERT_USERNAME_ID_LOCATOR = "input-email"
    INSERT_PASSWORD_ID_LOCATOR = "input-password"
    CLICK_LOGIN_BUTTON_CSS_SELECTOR = "input.btn"
    EDIT_ACCOUNT_LINK_CSS_SELECTOR = "#content>ul:nth-child(2)>li:nth-child(1)>a:nth-child(1)"

    def insert_username(self, username):
        self.driver.find_element(By.ID, self.INSERT_USERNAME_ID_LOCATOR).send_keys(username)

    def insert_password(self, password):
        self.driver.find_element(By.ID, self.INSERT_PASSWORD_ID_LOCATOR).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.CLICK_LOGIN_BUTTON_CSS_SELECTOR).click()

    def verify_edit_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.EDIT_ACCOUNT_LINK_CSS_SELECTOR).is_displayed()
