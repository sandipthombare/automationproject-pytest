import os, sys, pytest, pytest_html
 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as EdgeService
from pytest_html import extras


sys.path.append("C:\\Users\\sndpt\\OneDrive\\Desktop\\PY-TEST\\AutomationProjectEcom")


from src.main.utils.config_reader import read_properties
from src.main.utils.custom_logger import custom_log
from src.main.utils.report_generator import generate_html_report

script_directory = os.path.dirname(os.path.abspath(__file__))

logger = custom_log()
# dirr = os.path.join(script_directory,"../../")

# generate_html_report(dirr)
    

@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(script_directory, "../Configuration/config.properties")
    config = read_properties(config_path)

    logger.info("------------config---------------")
    return config


@pytest.fixture(scope="class", autouse=True)
def setup(request,config):

    logger.info("------------setup---------------")

    browser = config.get("default", "browser")
    url = config.get("default","url")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service =EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
         raise ValueError(f"Browser '{browser}' is not supported")
    
    driver.get(url)
    driver.maximize_window()
    
    request.cls.driver = driver
    request.cls.logger = logger

    yield 
    driver.quit()
    logger.info("------------test finished---------------")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.pluginmanager.import_plugin("pytest_html")
    screenshots_dir = os.path.join("src", "screen_shots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' and report.failed:  # Capture screenshot only if the test failed during the call phase
        driver = getattr(item.cls, 'driver', None)
        if driver:
            screenshot_path = "src/screen_shots/"f"{item.name}11.png"
            driver.save_screenshot(screenshot_path)
            
            extra_html = '<div><img src="%s" style="width:250px;height:200px;" '\
                        'onclick="window.open(this.src)" align="right"/></div>'%screenshot_path
            
            extra.append(pytest_html.extras.html(extra_html))

    report.extra = extra
