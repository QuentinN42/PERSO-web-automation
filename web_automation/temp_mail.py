"""
Temp mail
https://temp-mail.org/en/
"""

from .driver import Driver
from .functions import is_email


class TempMail(Driver):
    """
    Temp mail class.
    """
    
    base_url = "https://temp-mail.org/en/"
    
    @property
    def email(self) -> str:
        """
        Return the mail element (can be "Loading" or a valid email).
        """
        return self.driver.find_element_by_id("mail").get_property("value")
    
    def get_email(self) -> str:
        """
        Wait for the email.
        """
        while not is_email(self.email):
            pass
        return self.email
    
    def main(self, **kwargs) -> None:
        """
        Wait for the email and ...
        """
        print(self.get_email())
        
        input()
