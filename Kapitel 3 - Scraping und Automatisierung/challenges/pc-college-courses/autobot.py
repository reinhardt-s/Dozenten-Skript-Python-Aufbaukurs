from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement


class AutoBot:
    def __init__(self, headless=False):
        options = Options()
        options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    def goto_page(self, page: str):
        self.driver.get(page)
        print(f'Changed page to: {page}')

    def fill_input(self, selector: str, content: str):
        element = self.find_element(selector)
        element.clear()
        element.send_keys(content)
        return element

    def find_element(self, selector: str) -> WebElement:
        try:
            element = self.driver.find_element_by_xpath(selector)
        except NoSuchElementException:
            print("Element not found.")
            raise ElementMissingError
        return element

    def find_elements(self, selector: str) -> [WebElement]:
        elements = self.driver.find_elements_by_xpath(selector)
        return elements

    def click_element(self, selector: str):
        element = self.find_element(selector)
        element.click()

    def print_page(self):
        print(self.find_element('/html').get_attribute('outerHTML'))

    def __del__(self):
        self.driver.close()


class ElementMissingError(Exception):
    """Diese Ausnahme wird erzeugt, wenn ein angegebenes HTML-Element nicht gefunden wird"""

    def __init__(self):
        self.message = f"HTML element not found"
        super().__init__(self.message)
