"""
Temp mail
https://temp-mail.org/en/
"""

from .driver import Driver
from .functions import is_email


class TempMail(Driver):
    
    base_url = "https://temp-mail.org/en/"
    
    @property
    def email(self):
        return self.driver.find_element_by_id("mail").get_property("value")
    
    def get_email(self) -> str:
        while not is_email(self.email):
            pass
        return self.email
    
    def main(self) -> None:
        print(self.get_email())
        
        input()
