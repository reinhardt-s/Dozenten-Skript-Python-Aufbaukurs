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

text = "Contact us at contact@mywebsite.com or sales@mywebsite.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

for email in emails:
    print(email)

text = "Call us at 123-456-7890 or 098-765-4321"
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)

for number in phone_numbers:
    print(number)

text = "Important dates are 05-09-2022 and 12-25-2023"
dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)

for date in dates:
    print(date)

text = "Visit our website! www.mywebsite.com, best site ever!"
new_text = re.sub(r'www\.[\w\.-]+', '[redacted]', text)
print(new_text)

pattern = r"\d+"  # Das Muster passt auf eine oder mehrere Ziffern.
string = "12345 Hallo Welt!"

match = re.match(pattern, string)

# Match findet nur Übereinstimmungen am Anfang des Strings.
if match:
    print("Das Muster wurde gefunden!")
    print("Gefundene Übereinstimmung: ", match.group())  # Zeigt den Teil des Strings, der auf das Muster passt.
else:
    print("Das Muster wurde nicht gefunden.")

import re

pattern = r"\d+"  # Das Muster passt auf eine oder mehrere Ziffern.
string = "Hallo Welt! 12345 ist die Zahl."

match = re.search(pattern, string)

if match:
    print("Das Muster wurde gefunden!")
    print("Gefundene Übereinstimmung: ", match.group())  # Zeigt den Teil des Strings, der auf das Muster passt.
else:
    print("Das Muster wurde nicht gefunden.")

text = "1435:Lagemeldung bei eintreffen am Einsatzort" \
       "1444:Einsatzstelle an Polizei übergeben1450:Einsatzstelle verlassen"
# Teilen Sie den String jedes Mal, wenn "Welt" erscheint.
split_text = re.split('\d{4}:', text)

print(split_text)

