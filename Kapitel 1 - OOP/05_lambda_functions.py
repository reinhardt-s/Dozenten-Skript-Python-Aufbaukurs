calc = lambda a, b: a + b
print(calc(5, 4))


def how_many(text: str, symbol_1: str, symbol_2):
    finder = lambda l_text, symbol: l_text.lower().count(symbol)

    print(finder(text, symbol_1))
    print(finder(text, symbol_2))


how_many('“First, solve the problem. Then, write the code.” – John Johnson', 'j', 'o')


# https://www.flake8rules.com/rules/E731.html
# https://peps.python.org/pep-0008/#programming-recommendations
# Correct:
def def_f(x): return 2 ** x


# Wrong:
lambda_f = lambda x: 2 ** x


def calculate(x, calculate):
    # Setzt Euch auf Zeile 29 den Breakpoint
    # und schaut Euch im Debugger den Namen der
    # Übergebenen Funktion an.
    print(calculate(x))


calculate(4, lambda_f)
calculate(4, def_f)
