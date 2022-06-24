"""
Initializing Browser
Create base class which inherit setup class
Capture screenshot for failed test cases
Attach screenshot to the allure report
python add_option function which help the user to choose the browser at the run time
"""
import os
import time
from datetime import datetime
import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import find_dotenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="my option: chrome or firefox or edge",
    )
    parser.addoption(
        "--select_env",
        action="store",
        default="isc",
        help="my option: isc or kaplan or one_edu",
    )


def get_env(env_name):
    choose_env = {
        "isc": ".env-isc-rel",
        "kaplan": ".env-kaplan-rel",
        "one_edu": ".env-oneedu-rel",
        "isc-prod": ".env-isc-prod",
        "kaplan-prod": ".env-kaplan-prod",
    }
    load_dotenv(find_dotenv(filename=choose_env[env_name]))


@pytest.fixture(scope="class")
def setup(request):
    global driver

    select_env = request.config.getoption("select_env")
    print("Selected env ==", select_env)
    get_env(select_env)

    s1 = Service(ChromeDriverManager().install())
    s2 = Service(GeckoDriverManager().install())
    # s3 = Service(EdgeChromiumDriverManager().install())
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("window-size=1920x1480")

    browser_name = request.config.getoption("browser_name")
    print("browser name", browser_name)
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=s1, options=chrome_options)
    # elif browser_name == "edge":
    #     driver = webdriver.Edge(service=s3)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=s2)
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class BaseTestClass:
    pass


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs["setup"]
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


# make a screenshot with a name of the test, date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}'.replace(
        "/", "_"
    ).replace("::", "_")
    # file_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    driver.save_screenshot(os.path.join(BASE_DIR, "screenshots", file_name) + ".png")
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG,
    )

