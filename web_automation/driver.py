"""
Abstract class for all apps
"""
from abc import abstractmethod, ABC
from selenium import webdriver


class Driver(ABC):
    
    base_url: str = ""
    
    def __init__(self, base_url=None):
        self.driver = webdriver.Chrome()
        if base_url:
            self.base_url = base_url

    def connect(self) -> None:
        self.driver.get(self.base_url)

    def disconnect(self) -> None:
        self.driver.quit()

    @abstractmethod
    def main(self, *args, **kwargs) -> None:
        """
        Main method to implement
        """
        ...

    def execute(self, *args, **kwargs):
        self.connect()
        try:
            self.main(*args, **kwargs)
        finally:
            self.disconnect()
