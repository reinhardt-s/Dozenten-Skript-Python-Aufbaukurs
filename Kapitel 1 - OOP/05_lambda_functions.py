calc = lambda a, b: a + b
print(calc(5, 4))


def how_many(text: str, symbol_1: str, symbol_2):
    finder = lambda l_text, symbol: l_text.count(symbol)

    print(finder(text, symbol_1))
    print(finder(text, symbol_2))


def extract(file_1, file_2):
    beautify = lambda l_html: l_html.replace("_", " ")[:-4].title()
    # def b(l_html): return l_html.replace("_", " ")[:-4].title()

    print(beautify(file_1))
    print(beautify(file_2))
    # print(b(file_1))
    # print(b(file_2))

# https://www.flake8rules.com/rules/E731.html
def at_twelve(text):
    twelve = lambda at: at[12]
    def a_t(t): return t[12]
    print(a_t(text))
    print(twelve(text))


how_many("my name is bob", "b", "e")
extract("my_filename.txt", "orders.sql")
at_twelve("My name is earl")
at_twelve("I am Groot")
