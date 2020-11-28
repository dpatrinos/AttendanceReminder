from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import dotenv

class driver:
    def __init__(self):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        path = os.getenv("GECKODRIVER_PATH")
        self.driver = webdriver.Firefox(capabilities=cap, executable_path=path, options=options)

    def closeDriver(self):
        self.driver.close()

    def microsoftLogin(self, email, password):
        driver = self.driver
        driver.get("https://login.microsoftonline.com/")

        # input email address
        elem = driver.find_element_by_name("loginfmt")
        elem.send_keys(email)
        submitelem = driver.find_element_by_id("idSIButton9")
        submitelem.click()

        # input password
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "passwd"))
            )
        finally:
            elem.send_keys(password)
            elem.send_keys(Keys.ENTER)
            time.sleep(3)

    def getSrc(self):
        driver = self.driver
        driver.get("https://bphawks.schoology.com/course/2946961918/updates")
        time.sleep(5)
        img = driver.find_elements_by_tag_name("img")[14]
        return img.get_attribute("src")