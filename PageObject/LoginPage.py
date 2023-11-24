from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):  # This constructor get the driver from the actual test case
        # self.driver = driver    # Initiate the local driver and now the driver belong to the class then we can access the driver by using self keyword
        super().__init__(driver)  # super means the parent class which is the BasePage class

    INSERT_USERNAME_ID_LOCATOR = "input-email"
    INSERT_PASSWORD_ID_LOCATOR = "input-password"
    CLICK_LOGIN_BUTTON_CSS_SELECTOR = "input.btn"
    EDIT_ACCOUNT_LINK_CSS_SELECTOR = "#content>ul:nth-child(2)>li:nth-child(1)>a:nth-child(1)"
    WARNING_TEXT_CSS_SELECTOR = ".alert"

    def insert_username(self, username):
        # self.driver.find_element(By.ID, self.INSERT_USERNAME_ID_LOCATOR).send_keys(username)
        self.send_keys_to_element(By.ID, self.INSERT_USERNAME_ID_LOCATOR, username)

    def insert_password(self, password):
        # self.driver.find_element(By.ID, self.INSERT_PASSWORD_ID_LOCATOR).send_keys(password)
        self.send_keys_to_element(By.ID, self.INSERT_PASSWORD_ID_LOCATOR, password)

    def click_login_button(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.CLICK_LOGIN_BUTTON_CSS_SELECTOR).click()
        self.click_element(By.CSS_SELECTOR, self.CLICK_LOGIN_BUTTON_CSS_SELECTOR)

    def verify_edit_link(self):
        # self.driver.find_element(By.CSS_SELECTOR, self.EDIT_ACCOUNT_LINK_CSS_SELECTOR).is_displayed()
        self.is_element_displayed(By.CSS_SELECTOR, self.EDIT_ACCOUNT_LINK_CSS_SELECTOR)

    def login_warning_text(self):
        try:
        # self.driver.find_element(By.CSS_SELECTOR, self.WARNING_TEXT_CSS_SELECTOR).is_displayed()
            self.is_element_displayed(By.CSS_SELECTOR, self.WARNING_TEXT_CSS_SELECTOR)
        except NoSuchElementException as e:
            print(f"exception {e}")