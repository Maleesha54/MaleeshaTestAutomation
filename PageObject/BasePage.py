

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click_element(self, by, value):
        return self.driver.find_element(by, value).click()

    def send_keys_to_element(self, by, value, keys):
        return self.driver.find_element(by, value).send_keys(keys)

    def is_element_displayed(self, by, value):
        return self.driver.find_element(by, value).is_displayed()

