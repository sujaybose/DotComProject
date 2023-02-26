import pytest
from pageObjects.FlightsPage import Flights
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    url = ReadConfig.get_url()
    from_location = ReadConfig.from_location()
    to_location = ReadConfig.to_location()
    depart_date = ReadConfig.depart_date()
    return_date = ReadConfig.return_date()
    logger = LogGen.loggen()
    logger.info("****Started Logging Test Info ****")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_flights_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home Page Title Test ****")
        self.driver = setup
        self.driver.get(self.url)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "JetBlue | Airline Tickets, Flights & Airfare: Book Direct - Official Site":
            assert True
        else:
            assert False

    @pytest.mark.regression
    def test_flightSearch_loginPageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Flight Search Test ****")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.fl = Flights(self.driver)
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame(1)
        self.driver.implicitly_wait(5)
        self.fl.button_cookies_accept()
        self.driver.switch_to.default_content()
        self.fl.set_from_location(self.from_location)
        self.fl.set_to_location(self.to_location)
        self.driver.implicitly_wait(5)
        self.fl.set_depart_date(self.depart_date)
        self.driver.implicitly_wait(5)
        self.fl.set_return_date(self.return_date)
        self.driver.implicitly_wait(5)
        self.fl.button_search_flight_click()
        self.driver.implicitly_wait(20)
        act_title1 = self.driver.title
        print(act_title1)
        self.driver.close()
        if act_title1 == "JetBlue | Select Flights":
            assert True
        else:
            assert False

