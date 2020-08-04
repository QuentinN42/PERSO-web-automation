"""
Temp mail
https://temp-mail.org/en/
"""
from .driver import Driver


class TempMail(Driver):
    
    base_url = "https://temp-mail.org/en/"
    
    def main(self) -> None:
        input()
