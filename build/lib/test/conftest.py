import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as EdgeService
# import sys
import sys
sys.path.append("C:\\Users\\sndpt\\OneDrive\\Desktop\\PY-TEST\\AutomationProjectEcom")

# sys.path.insert(1,'C://Users//sndpt//OneDrive//Desktop//PY-TEST//AutomationProjectEcom//src//main//utils')
print(sys.path)
# import config_reader
from src.main.utils.config_reader import read_properties

script_directory = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session")
def config():
    config = read_properties(script_directory + "../../Configuration/config.properties")
    return config


@pytest.fixture(scope="class", autouse=True)
def setup(request,config):

    browser = config.get("DEFAULT", "browser")
    url = config.get("DEFAULT", "url")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service =EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
         raise ValueError(f"Browser '{browser}' is not supported")
    
    driver.get(url)
    request.cls.driver = driver

    yield 

    driver.quit()



