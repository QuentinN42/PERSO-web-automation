"""
Temp mail
https://temp-mail.org/en/
"""

from .driver import Driver
from .functions import is_email


class TempMail(Driver):
    
    base_url = "https://temp-mail.org/en/"
    
    def get_mail(self) -> str:
        while not is_email(mail := self.driver.find_element_by_id("mail").get_property("value")):
            pass
        return mail
    
    def main(self) -> None:
        print(self.get_mail())
        
        input()
