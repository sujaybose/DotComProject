from selenium.webdriver.common.by import By

class Flights:
    button_iframe_xpath = "//a[text()= 'Accept All Cookies']"
    textbox_fromLoc_xpath ="//label[contains(text(),'From')]//following-sibling::input"
    drop_fromLoc_xpath= "//strong[starts-with(text(), 'New York')]"
    textbox_toLoc_xpath ="//label[contains(text(),'To')]//following-sibling::input"
    drop_tomLoc_xpath = "//strong[starts-with(text(), 'Seattle')]"
    textbox_depart_xpath ="//label[contains(text(),'Depart')]//following-sibling::input"
    drop_depart_xpath= "//span[contains(text(), 'Done')]"
    textbox_return_xpath = "//label[contains(text(),'Return')]//following-sibling::input"
    drop_return_xpath = "//span[contains(text(), 'Done')]"
    button_searchFlight_xpath = "//span[contains(text(),'Search flights')]"

    def __init__(self, driver):
        self.driver = driver

    def button_cookies_accept(self):
        self.driver.find_element(By.XPATH, self.button_iframe_xpath).click()

    def set_from_location(self, from_location):
        self.driver.find_element(By.XPATH, self.textbox_fromLoc_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_fromLoc_xpath).send_keys(from_location)
        self.driver.find_element(By.XPATH, self.drop_fromLoc_xpath).click()

    def set_to_location(self, to_location):
        self.driver.find_element(By.XPATH, self.textbox_toLoc_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_toLoc_xpath).send_keys(to_location)
        self.driver.find_element(By.XPATH, self.drop_tomLoc_xpath).click()

    def set_depart_date(self, depart_date):
        self.driver.find_element(By.XPATH, self.textbox_depart_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_depart_xpath).send_keys(depart_date)
        self.driver.find_element(By.XPATH, self.drop_depart_xpath).click()

    def set_return_date(self, return_date):
        try:
            # self.driver.find_element(By.XPATH, self.textbox_return_xpath).clear()
            self.driver.find_element(By.XPATH, self.textbox_return_xpath).send_keys(return_date)
            self.driver.find_element(By.XPATH, self.drop_return_xpath).click()
        except:
            print("element not found in return date")
            # self.driver.find_element(By.XPATH, self.button_searchFlight_xpath).click()

    def button_search_flight_click(self):
        print("Click on search Flight")
        self.driver.find_element(By.XPATH, self.button_searchFlight_xpath).click()



