from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.google.com')

accept_terms = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
accept_terms.click()

search_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_input.send_keys('Bars in Berlin')
search_input.send_keys(Keys.RETURN)

bars = driver.find_elements_by_class_name('rllt__details')


@dataclass()
class Bar:
    name: str
    rating: float
    type: str
    location: str
    opens: str
    style: str

    def __gt__(self, other):
        return True if self.rating > other.rating else False

    def __lt__(self, other):
        return True if self.rating < other.rating else False

    def __eq__(self, other):
        return True if self.rating == other.rating else False

    def __le__(self, other):
        return True if self.rating <= other.rating else False

    def __ge__(self, other):
        return True if self.rating >= other.rating else False


recommendations = []
recommendations_as_classes = []

for bar in bars:
    as_list = bar.text.split('\n')
    recommendations.append(dict(zip(['name', 'rating', 'type', 'location', 'opens', 'style'], as_list)))
    recommendations_as_classes.append(
        Bar(name=as_list[0], rating=float(as_list[1].replace(',', '.')), type=as_list[2], location=as_list[3],
            opens=as_list[4], style=as_list[5]))

for bar in recommendations:
    print(bar['name'])

print(recommendations_as_classes)
recommendations_as_classes.sort(reverse=True)
print(recommendations_as_classes)
driver.close()
