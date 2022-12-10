from course import Course
from autobot import AutoBot, ElementMissingError

autobot = AutoBot()
courses_bot = AutoBot()
course_bot = AutoBot()
course_list = []


def extract_cost(text: str):
    start = 3 if text.startswith('ab') else 0
    return int(text[start:-5].replace(".", ""))


def extract_duration(text: str):
    return int(text[12:-32])


def add_course():
    name = course_bot.find_element('//*[@id="sp1"]/h1').text

    try:
        cost_element = course_bot.find_element('//*[@id="sp2_1"]/div/p[2]/span').text
    except ElementMissingError:
        print(">>> Kurs hat keinen Preis angegeben.")
        return
    cost = extract_cost(cost_element)

    duration_element = course_bot.find_element('//*[@id="zeit"]').text
    duration = extract_duration(duration_element)

    course_list.append(Course(name=name, cost=cost, duration=duration))


def read_courses(link: str):
    courses_bot.goto_page(link)

    course_list_elements = courses_bot.find_elements('/html/body/div[1]/div/div/div[2]/div/ul/li')
    for course_list_element in course_list_elements:
        course_bot.goto_page(course_list_element.find_element_by_css_selector('a').get_attribute('href'))
        add_course()


autobot.goto_page(page='https://www.pc-college.de')
# Bestätige Cookies
autobot.click_element(selector='//*[@id="clayer"]/div/button[1]')
# Fülle Suchfeld aus
autobot.fill_input(selector='/html/body/div[1]/header/form/div/input[1]', content='Einführung')
# Click Suchen Button
autobot.click_element(selector='/html/body/div[1]/header/form/div/input[2]')

# Erstelle Liste der Ergebnisseiten
element_list = autobot.find_elements('//*[@id="sp1"]/nav[1]/a')
for count, page in enumerate(element_list, start=1):
    print(f'Seite: {count} -> {page.get_attribute("href")}')
    read_courses(page.get_attribute('href'))

    # Nur die ersten drei Seiten
    if count == 3:
        break

course_list.sort()
print(course_list)
print(f'Günstigste Kurs: {course_list[0].name}')
print(f'Teuerste Kurs: {course_list[-1].name}')
