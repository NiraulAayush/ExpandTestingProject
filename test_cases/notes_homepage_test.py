import unittest
import time

from selenium import webdriver
from ExpandTestingProject.pages.create_account import CreateAccount
from ExpandTestingProject.pages.register_account import RegisterPage


class NoteHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_note_app_valid(self):    #test method name must start with test_method_name

        driver = self.driver
        driver.get("https://practice.expandtesting.com/notes/app")

        create_account = CreateAccount(driver)
        create_account.click_create_account_btn()


        register_page = RegisterPage(driver)
        register_page.enter_email("wohate4047@cotigz.com")
        register_page.enter_name("Wortz Cohtz")
        register_page.enter_password("Admin@112")
        register_page.enter_confirm_password("Admin@112")
        register_page.click_register_btn()

        time.sleep(3)
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()