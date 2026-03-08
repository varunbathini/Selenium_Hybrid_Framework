import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from Utilities.read_properties import Read_Config
from Utilities.custom_logger import Log_Maker
from Utilities import excel_utils

class Test_02_Admin_Login_data_driven:

    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//Test_data//Admin_login-data.xlsx"

    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("**********test_valid_admin_login_data_driven started************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(".//Test_data//Admin_login-data.xlsx","Sheet1")
        print("num of rows",self.rows)



        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_log()
        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text
        if act_dashboard_text == "Dashboard":
            self.logger.info("**********Dashboard text found ************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False










