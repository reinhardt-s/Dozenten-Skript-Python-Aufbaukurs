from dataclasses import dataclass
from typing import List

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@dataclass()
class Bar:
    name: str
    rating: float
    type: str
    location: str
    opens: str
    style: str

    def __gt__(self, other):
        return self.rating > other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __ge__(self, other):
        return self.rating >= other.rating


def get_bars(driver: webdriver.Chrome, search_term: str) -> List[Bar]:
    driver.get('http://www.google.com')
    accept_terms = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
    accept_terms.click()

    search_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_input.send_keys(search_term)
    search_input.send_keys(Keys.RETURN)

    bars = driver.find_elements_by_class_name('rllt__details')

    recommendations = []
    for bar in bars:
        as_list = bar.text.split('\n')
        if len(as_list) < 6:
            as_list.append(as_list[4])
            as_list[4] = 'unbekannt'
        recommendations.append(
            Bar(name=as_list[0], rating=float(as_list[1].replace(',', '.')), type=as_list[2], location=as_list[3],
                opens=as_list[4], style=as_list[5]))

    return recommendations


if __name__ == '__main__':
    driver = webdriver.Chrome()
    bars = get_bars(driver, 'Bars in Berlin')
    for bar in bars:
        print(bar.name)
    bars.sort(reverse=True)
    print(bars)
    driver.close()
