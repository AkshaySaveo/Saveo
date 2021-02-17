from Pages.WebGeneric import WebGeneric
class LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.un_id="mat-input-0"
        #aself.pwd_name=
        self.login_btn_xpath="//*[@id='sign-in-button']/span"
        self.otp_btn='//*[@placeholder="Enter OTP here"]'
        self.submit_btn='//span[text()="Verify"]'
        self.wg=WebGeneric(self.driver)

    def acti_login(self):
        # Logint to application - section 2 >>S2
        #self.driver.find_element_by_id("username").send_keys("admin")
        #un= self.wg.get_val("Login","UserName")
        self.wg.enter("id", self.un_id, "7701930106")
        #self.wg.enter("name",self.pwd_name,"manager")
        #self.driver.find_element_by_name("pwd").send_keys("manager")
        self.wg.submit("xpath", self.login_btn_xpath)
        self.wg.enter("xpath", self.otp_btn, '987654')
        self.wg.submit("xpath", self.submit_btn)
