"""
Temp mail
https://temp-mail.org/en/
"""
from time import sleep

from .driver import Driver
from selenium.webdriver.support.ui import WebDriverWait


class TempMail(Driver):
    
    base_url = "https://temp-mail.org/en/"
    
    def get_mail(self) -> str:
        while (mail := self.driver.find_element_by_id("mail").get_property("value")) in ["", "Loading ..."]:
            pass
        return mail
    
    def main(self) -> None:
        # print(self.get_mail())
        sleep(5)
        print(self.get_mail())
        
        input()
