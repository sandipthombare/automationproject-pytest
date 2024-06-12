from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import logging

from src.main.base.base_config import BaseDriver

class SigninCreateAc(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)


    SIGN_IN          = "//a[contains(text(),'Sign in')]"
    # signin
    EMAIL_INPUT1     = "//input[@id='email']"
    PASSWORD         = "(//input[@id='passwd'])[1]"
    SIGN_IN_BTN      = "//button[@id='SubmitLogin']"    
    #createaccount 
    EMAIL_INPUT      = "//input[@id='email_create']"
    CREATE_AC_BTN    = "//button[@id='SubmitCreate']"
    TITLE_MR         = "//div[@id='uniform-id_gender1']"
    TITLE_MRS        = "//input[@id='id_gender2']"
    FIRST_NAME       = "//input[@id='customer_firstname']"
    LAST_NAME        = "//input[@id='customer_lastname']"
    PASSWORD1        = "//input[@id='passwd']"
    DATE_DAY         = "//select[@id='days']"
    DATE_MONTH       = "//select[@id='months']"
    DATE_YEAR        = "//select[@id='years']"
    SUBMIT           = "//button[@id='submitAccount']"
    AC_CONFIRM       = "//p[@class='alert alert-success']"
# createaccount
    def getSignInPage(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SIGN_IN)
    
    def getEmaiIp(self):
        return self.wait_for_presence_of_element(By.XPATH, self.EMAIL_INPUT)
    
    def getCreateAcBtn(self):
        return self.wait_for_presence_of_element(By.XPATH, self.CREATE_AC_BTN)
    
    def getTitle(self, title):
        if title == 'Mr':
            self.wait_for_presence_of_element(By.XPATH, self.TITLE_MR).click()
        else:
            self.wait_for_presence_of_element(By.XPATH, self.TITLE_MRS).click()



    def getFirstName(self):
        return self.wait_for_presence_of_element(By.XPATH, self.FIRST_NAME)
    
    def getLastName(self):
        return self.wait_for_presence_of_element(By.XPATH, self.LAST_NAME)
    
    def getPassword(self):
        return self.wait_for_presence_of_element(By.XPATH, self.PASSWORD1)
    
    def select_date(self, day, month,year):
        day_dropdown = Select(self.driver.find_element(By.XPATH, self.DATE_DAY))
        month_dropdown = Select(self.driver.find_element(By.XPATH, self.DATE_MONTH))
        year_dropdown = Select(self.driver.find_element(By.XPATH, self.DATE_YEAR))

        time.sleep(2)
        day_dropdown.select_by_value(str(day))
        month_dropdown.select_by_value(str(month))
        year_dropdown.select_by_value(str(year))
        time.sleep(2)

    def getDateMonth(self):
        return self.wait_for_presence_of_element(By.XPATH, self.DATE_MONTH)
    
    def getDateYear(self):
        return self.wait_for_presence_of_element(By.XPATH, self.DATE_YEAR)
    
    def getSubmitBtn(self):
        return self.wait_for_presence_of_element(By.XPATH, self.SUBMIT)
    
    def accountConf(self) -> bool:
        try:
            element = self.wait_for_presence_of_element(By.XPATH, self.AC_CONFIRM).text
            return element == "Your account has been created."
        except Exception:
            return False

# signin
    def getEmailInput(self):
        return self.wait_for_presence_of_element(By.XPATH, self.EMAIL_INPUT1)
    
    def getPassInput(self):
        return self.wait_for_presence_of_element(By.XPATH, self.PASSWORD)
    
    def getSigninBtn(self):
        return self.wait_for_presence_of_element(By.XPATH, self.SIGN_IN_BTN)
    
