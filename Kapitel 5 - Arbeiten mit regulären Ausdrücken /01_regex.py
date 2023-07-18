# https://docs.python.org/3/library/re.html

# Reguläre Ausdrücke (regex) sind ein mächtiges Werkzeug in der Programmierung, um Textmuster zu finden, zu überprüfen und zu manipulieren. In Python wird das re-Modul verwendet, um mit regulären Ausdrücken zu arbeiten. Hier sind einige grundlegende Funktionen und Beispiele:
#
# re.match(pattern, string): Überprüft, ob das Muster am Anfang des Strings vorhanden ist.
#
# re.search(pattern, string): Sucht das Muster irgendwo im String.
#
# re.findall(pattern, string): Gibt alle Übereinstimmungen des Musters im String als Liste von Strings zurück. Die Liste enthält die Übereinstimmungen in der Reihenfolge, in der sie im String gefunden werden.
#
# re.split(pattern, string, [maxsplit=0]): Teilt den String durch das Auftreten des Musters.
#
# re.sub(pattern, repl, string, [count=0]): Ersetzt alle Übereinstimmungen des Musters im String durch eine Ersatzzeichenkette.
#
# Bevor wir in die Beispiele einsteigen, hier ist ein kurzer Überblick über einige übliche Regex-Muster:
#
# . : Jedes einzelne Zeichen außer Zeilenumbruch
# ^ : Start der Zeichenkette
# $ : Ende der Zeichenkette
# * : Null oder mehr Wiederholungen
# + : Eine oder mehr Wiederholungen
# ? : Null oder eine Wiederholung
# \d : Ziffern (0-9)
# \D : Nicht-Ziffern
# \s : Weißraum (Leerzeichen, Tab, Zeilenumbruch etc.)
# \S : Nicht-Weißraum
# \w : Alphanumerische Zeichen (a-z, A-Z, 0-9) und Unterstrich (_)
# \W : Nicht-Wort-Zeichen


import re

def find_emails(text):
    """
    Find all email addresses in a given text.

    Args:
    text (str): The text to search for email addresses.

    Returns:
    list: A list of email addresses found in the text.
    """
    return re.findall(r'[\w\.-]+@[\w\.-]+', text)

def find_phone_numbers(text):
    """
    Find all phone numbers in a given text.

    Args:
    text (str): The text to search for phone numbers.

    Returns:
    list: A list of phone numbers found in the text.
    """
    return re.findall(r'\d{3}-\d{3}-\d{4}', text)

def find_dates(text):
    """
    Find all dates in a given text.

    Args:
    text (str): The text to search for dates.

    Returns:
    list: A list of dates found in the text.
    """
    return re.findall(r'\d{2}-\d{2}-\d{4}', text)

def redact_website(text):
    """
    Replace all website URLs in a given text with [redacted].

    Args:
    text (str): The text to search for website URLs.

    Returns:
    str: The text with website URLs replaced with [redacted].
    """
    return re.sub(r'www\.[\w\.-]+', '[redacted]', text)

def find_numbers_at_start(text):
    """
    Find the first occurrence of a number at the start of a given text.

    Args:
    text (str): The text to search for a number at the start.

    Returns:
    str: The first number found at the start of the text, or None if no number is found.
    """
    match = re.match(r"\d+", text)
    if match:
        return match.group()
    else:
        return None

def find_number_in_text(text):
    """
    Find the first occurrence of a number in a given text.

    Args:
    text (str): The text to search for a number.

    Returns:
    str: The first number found in the text, or None if no number is found.
    """
    match = re.search(r"\d+", text)
    if match:
        return match.group()
    else:
        return None

def split_text_by_numbers(text):
    """
    Split a given text by numbers.

    Args:
    text (str): The text to split.

    Returns:
    list: A list of strings split by numbers.
    """
    return re.split('\d{4}:', text)

# Example usage
text = "Contact us at contact@mywebsite.com or sales@mywebsite.com"
emails = find_emails(text)
print(emails)

text = "Call us at 123-456-7890 or 098-765-4321"
phone_numbers = find_phone_numbers(text)
print(phone_numbers)

text = "Important dates are 05-09-2022 and 12-25-2023"
dates = find_dates(text)
print(dates)

text = "Visit our website! www.mywebsite.com, best site ever!"
new_text = redact_website(text)
print(new_text)

text = "12345 Hallo Welt!"
number_at_start = find_numbers_at_start(text)
print(number_at_start)

text = "Hallo Welt! 12345 ist die Zahl."
number_in_text = find_number_in_text(text)
print(number_in_text)

text = "1435:Lagemeldung bei eintreffen am Einsatzort" \
       "1444:Einsatzstelle an Polizei übergeben1450:Einsatzstelle verlassen"
split_text = split_text_by_numbers(text)
print(split_text)
