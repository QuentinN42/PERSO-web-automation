"""
Abstract class for all apps.
"""
from abc import abstractmethod, ABC

from selenium import webdriver


class Driver(ABC):
    """
    Abstract Driver class.
    """
    
    base_url: str = ""
    
    def __init__(self, base_url=None):
        """
        Init the web browser.
        """
        self.driver = webdriver.Chrome()
        if base_url:
            self.base_url = base_url
    
    def connect(self) -> None:
        """
        Connect to the base url.
        """
        self.driver.get(self.base_url)
    
    def disconnect(self) -> None:
        """
        Disconnect and close the browser.
        """
        self.driver.quit()

    @abstractmethod
    def main(self, **kwargs) -> None:
        """
        Main method to implement
        """
        ...
    
    def execute(self, disconnect: bool = True, **kwargs):
        """
        Connect, execute the main script and disconnect.
        """
        self.connect()
        try:
            self.main(**kwargs)
        finally:
            if disconnect:
                self.disconnect()
