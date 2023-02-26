import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching firefox browser.........")     #Read:https://pypi.org/project/webdriver-manager
    elif browser=='edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching edge browser.........")
    else:
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        print("Launching ie browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'SeleniumAutomation'
    config._metadata['Module Name'] = 'DotCom'
    config._metadata['Tester'] = 'Sujay'
    config._metadata['Browser'] = config.getoption("--browser")

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
