from selenium import webdriver
from Pages.Loginpage import LoginPage
from Pages.dashbordpage import DashbrdPage
from Pages.RetrievePage import RetrievePage
from Pages.madicinepage import HomePage
import pytest

@pytest.mark.usefixtures("test_setup")
class  TestLogin:
    def test_login(self):
        driver=self.driver
        lp=LoginPage(driver)
        lp.acti_login()

    def test_dashbrd(self):
         driver = self.driver
         tp = DashbrdPage(driver)
         tp.task_login()

    # @pytest.mark.skip
    #
    def test_home(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.Home_login()

    def test_report(self):
        driver = self.driver
        rp = RetrievePage(driver)
        rp.Report_login()


