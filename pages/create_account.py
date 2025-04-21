from selenium.webdriver.common.by import By

class CreateAccount:

    def __init__(self, driver):
        self.driver = driver
        self.create_account_link_text = "Create an account"

    def click_create_account_btn(self):
        self.driver.find_element(By.LINK_TEXT,self.create_account_link_text).click()