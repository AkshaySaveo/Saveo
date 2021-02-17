from Pages.WebGeneric import WebGeneric
class RetrievePage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.reports_btn_id= "/html/body/app-root/div/app-dashboard-container/div/mat-drawer-container/mat-drawer-content/mat-sidenav-container/mat-sidenav-content/mat-toolbar/mat-toolbar-row[1]/div[2]/a[3]/span"
        self.admin_dash_xpath='//*[@id="cdk-overlay-5"]/div/div/span/a[2]'
        self.menu='//mat-icon[@id="menu"]'
        self.ord_plc_btn='//span[contains(text(),"Order Placing")]'
        self.retrv_btn='//*[contains(text(),"Order Retrieve")]'
        #self.retv_check='//*[@id="mat-checkbox-87"]/label/div'
        self.re_n_mail="//*[contains(text(),'Retrieve & Email')]"
        self.wg=WebGeneric(self.driver)

    def Report_login(self):
        import time
        time.sleep(4)
        self.wg.submit("xpath", self.reports_btn_id)
        self.wg.submit("xpath", self.admin_dash_xpath)
        self.wg.submit("xpath", self.menu)
        self.wg.submit("xpath", self.ord_plc_btn)
        self.wg.submit("xpath", self.retrv_btn)
        time.sleep(5)
        #self.wg.submit("xpath", self.retv_check)
        self.wg.submit("xpath", self.re_n_mail)
