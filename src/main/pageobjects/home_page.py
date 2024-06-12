import pytest

@pytest.markup.fixtures()
class Home_Page:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def home_page(self):
        self.driver.get(self.url)

    