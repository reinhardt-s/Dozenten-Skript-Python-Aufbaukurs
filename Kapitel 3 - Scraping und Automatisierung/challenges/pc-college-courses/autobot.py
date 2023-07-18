from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement


from typing import List
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement


class ElementMissingError(Exception):
    """Raised when an HTML element is not found"""

    def __init__(self):
        self.message = f"HTML element not found"
        super().__init__(self.message)


class AutoBot:
    def __init__(self, headless: bool = False):
        options = Options()
        options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    def goto_page(self, page: str) -> None:
        """Navigates to the specified page"""
        self.driver.get(page)
        print(f'Changed page to: {page}')

    def fill_input(self, selector: str, content: str) -> WebElement:
        """Finds the input element specified by the selector and fills it with the given content"""
        element = self.find_element(selector)
        element.clear()
        element.send_keys(content)
        return element

    def find_element(self, selector: str) -> WebElement:
        """Finds the first element that matches the specified selector"""
        try:
            element = self.driver.find_element_by_xpath(selector)
        except NoSuchElementException:
            print("Element not found.")
            raise ElementMissingError
        return element

    def find_elements(self, selector: str) -> List[WebElement]:
        """Finds all elements that match the specified selector"""
        elements = self.driver.find_elements_by_xpath(selector)
        return elements

    def click_element(self, selector: str) -> None:
        """Finds the element specified by the selector and clicks it"""
        element = self.find_element(selector)
        element.click()

    def print_page(self) -> None:
        """Prints the outer HTML of the entire page"""
        print(self.find_element('/html').get_attribute('outerHTML'))

    def __del__(self):
        """Closes the browser window when the object is deleted"""
        self.driver.close()
