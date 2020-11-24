import dotenv
import os
from webdriver import driver
import urllib.request
from datetime import datetime

email = os.getenv("MICRO_E")
password = os.getenv("MICRO_P")

main_driver = driver()

def getQuotePic():
    main_driver.microsoftLogin(email, password)
    src = main_driver.getSrc()
    print(src)
    file = urllib.request.urlretrieve(src)

getQuotePic()
main_driver.closeDriver()
