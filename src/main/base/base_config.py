import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def page_scroll(self):
        scroll_pause_time = 2

        while True:
            current_scroll_height = self.driver.execute_script("return document.body.scrollHeight")

            self.driver.execute_script(f"window.scrollTo(0, {current_scroll_height})")
            
            time.sleep(scroll_pause_time)

            new_scroll_height = self.driver.execute_script("return document.body.scrollHeight")
            
            if(current_scroll_height == new_scroll_height):
                break
    
    def wait_for_presence_of_element(self, locator_type, locator):
        element =  self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element
    
    def wait_until_element_is_clickable(self,locator_type, locator):
        element =  self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element