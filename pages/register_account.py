from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self,driver):
        self.driver = driver
        self.email_id = "email"
        self.name_id = "name"
        self.password_id = "password"
        self.confirm_password_id = "confirmPassword"
        self.register_btn_xpath = "/html/body/main/div[3]/div[2]/div/div/div/div/div/div/div/div/form/div[2]/button"

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.email_id).send_keys(email)

    def enter_name(self,name):
        self.driver.find_element(By.ID,self.name_id).send_keys(name)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,self.confirm_password_id).send_keys(confirm_password)

    def click_register_btn(self):
        self.driver.find_element(By.XPATH,self.register_btn_xpath).click()