import  pytest
from selenium.webdriver.common.by import By
import time , datetime
import sys
sys.path.append("C:\\Users\\sndpt\\OneDrive\\Desktop\\PY-TEST\\AutomationProjectEcom")

from src.main.pageobjects.signin_createac import SigninCreateAc
from src.main.utils.data_reader import read_json


@pytest.mark.usefixtures("setup")
class TestSigninCreateAccount:

    
    @classmethod
    def setup_class(cls):
        try:
            file_path = "src\\main\\dataprovider\\account_data.json"
            cls.data = read_json(file_path)

        except Exception as e:
            pytest.fail(f"An error occured while reading file{e} ")

    def test_create_ac(self):
        
            self.logger.info("------------TC001---------------")
            self.logger.info("TESTCASE INITIALIZED")

            sp = SigninCreateAc(self.driver)
            sp.getSignInPage().click()
            self.logger.info("Navigated to Sign In Page")

            # self.driver.save_screenshot("src/screen_shots/sq1.png")
            
            sp.getEmaiIp().send_keys(self.data['email'])
            self.logger.info(f"Entered email: {self.data['email']}")
            time.sleep(2)

            sp.getCreateAcBtn().click()
            self.logger.info("Clicked Create Account button")
            time.sleep(2)

            sp.getTitle(self.data['title'])
            self.logger.info(f"Selected title: {self.data['title']}")
            time.sleep(2)

            sp.getFirstName().send_keys(self.data['first_name'])
            self.logger.info(f"Selected first name: {self.data['first_name']}")
            time.sleep(2)

            sp.getLastName().send_keys(self.data['last_name'])
            self.logger.info(f"Selected last name: {self.data['last_name']}")
            time.sleep(2)

            sp.getPassword().send_keys(self.data['password'])
            self.logger.info("Entered password")
            time.sleep(2)

            sp.select_date(self.data['dob']['day'],self.data['dob']['month'],self.data['dob']['year'])
            self.logger.info(f"Selected date of birth: {self.data['dob']['day']}-{self.data['dob']['month']}-{self.data['dob']['year']}")
            time.sleep(10)

            sp.getSubmitBtn().click()
            self.logger.info("Clicked submit button")
            time.sleep(10)

            if(sp.accountConf()):
                self.logger.info("TESTCASE PASSED")
                assert  True

            else:
                self.logger.info("TESTCASE FAILED")
                assert False

            time.sleep(10)
        
