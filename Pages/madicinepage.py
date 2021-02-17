from Pages.WebGeneric import WebGeneric
import time
class HomePage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.serch_className= "/html/body/app-root/div/app-dashboard-container/div/mat-drawer-container/mat-drawer-content/mat-sidenav-container/mat-sidenav-content/mat-toolbar/mat-toolbar-row[1]/app-search-bar/form/div/input"
        self.add_btn_xpath='//*[@class="mat-button-wrapper"]'
        self.qty = '//*[@id="dashboard-container"]/div/div[3]/app-common-search-container/div/div[1]/table/tr/td[6]/div[1]/div/div[1]/div/input'
        self.cnfm = "//*[@class='mat-button-wrapper']"
        self.cart = "/html/body/app-root/div/app-dashboard-container/div/mat-drawer-container/mat-drawer-content/mat-sidenav-container/mat-sidenav-content/mat-toolbar/mat-toolbar-row[1]/div[2]/a[2]/span"
        self.slt = "mat-radio-2"   #//input[contains(@value, "SLOT_TWO")]
        self.plc_ord='//*[@id="dashboard-content"]/mat-drawer-container/mat-drawer/div/div[2]/div[7]/button/span'
        self.wg=WebGeneric(self.driver)

    def Home_login(self):
        self.wg.enter("xpath", self.serch_className, "Sinarest Drops(p)")
        time.sleep(5)
        self.wg.submit("xpath", self.add_btn_xpath)
        self.wg.submit1("xpath", self.qty, '17')
        self.wg.submit("xpath", self.cnfm)
        time.sleep(5)
        self.wg.submit("xpath",self.cart)
        time.sleep(5)
        self.wg.submit('id', self.slt)
        time.sleep(3)
        self.wg.submit('xpath', self.plc_ord)
        time.sleep(4)




