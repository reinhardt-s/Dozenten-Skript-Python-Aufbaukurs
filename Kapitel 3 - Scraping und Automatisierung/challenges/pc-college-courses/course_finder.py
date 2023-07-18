from course import Course
from autobot import AutoBot, ElementMissingError


# Create AutoBot instances
autobot = AutoBot()
courses_bot = AutoBot()
course_bot = AutoBot()

# Create an empty list to store courses
course_list = []


def extract_cost(text: str) -> int:
    """Extracts the cost of a course from a string"""
    start = 3 if text.startswith('ab') else 0
    return int(text[start:-5].replace(".", ""))


def extract_duration(text: str) -> int:
    """Extracts the duration of a course from a string"""
    return int(text[12:-32])


def add_course() -> None:
    """Adds a course to the course_list"""
    name = course_bot.find_element('//*[@id="sp1"]/h1').text

    try:
        cost_element = course_bot.find_element('//*[@id="sp2_1"]/div/p[2]/span')
    except ElementMissingError:
        print(">>> Kurs hat keinen Preis angegeben.")
        return
    cost = extract_cost(cost_element.text)

    duration_element = course_bot.find_element('//*[@id="zeit"]')
    duration = extract_duration(duration_element.text)

    course_list.append(Course(name=name, cost=cost, duration=duration))


def read_courses(link: str) -> None:
    """Reads courses from a given link and adds them to the course_list"""
    courses_bot.goto_page(link)

    course_list_elements = courses_bot.find_elements('/html/body/div[1]/div/div/div[2]/div/ul/li')
    for course_list_element in course_list_elements:
        course_bot.goto_page(course_list_element.find_element_by_css_selector('a').get_attribute('href'))
        add_course()


# Go to the PC-College website
autobot.goto_page(page='https://www.pc-college.de')

# Accept cookies
autobot.click_element(selector='//*[@id="clayer"]/div/button[1]')

# Search for courses
autobot.fill_input(selector='/html/body/div[1]/header/form/div/input[1]', content='Einführung')
autobot.click_element(selector='/html/body/div[1]/header/form/div/input[2]')

# Get a list of result pages
element_list = autobot.find_elements('//*[@id="sp1"]/nav[1]/a')

# Read courses from the first three pages
for count, page in enumerate(element_list, start=1):
    print(f'Seite: {count} -> {page.get_attribute("href")}')
    read_courses(page.get_attribute('href'))

    if count == 3:
        break

# Sort the course list
course_list.sort()

# Print the course list and the cheapest/most expensive courses
print(course_list)
print(f'Günstigste Kurs: {course_list[0].name}')
print(f'Teuerste Kurs: {course_list[-1].name}')
