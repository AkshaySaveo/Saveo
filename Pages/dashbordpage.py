from Pages.WebGeneric import WebGeneric
class DashbrdPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.id="menu"
        self.addNw_btn_xpath="//img[@class='tb-image']"
        # self.newcustmr_btn_xpath="//div[text()='+ New Customer']"
        # self.cancel_btn_xpath = '//*[@id="customerLightBoxCloseButton"]'
        self.wg=WebGeneric(self.driver)

    def task_login(self):
        # Logint to application - section 2 >>S2
        #self.driver.find_element_by_id("username").send_keys("admin")
        #un= self.wg.get_val("Login","UserName")

        #self.driver.find_element_by_name("pwd").send_keys("manager")
        self.wg.submit("id", self.id)
        self.wg.submit("xpath", self.addNw_btn_xpath)
        #self.wg.submit("xpath", self.newcustmr_btn_xpath)
        # print('needs to click on cancel')
        # self.wg.submit("xpath", self.addNw_btn_xpath)
