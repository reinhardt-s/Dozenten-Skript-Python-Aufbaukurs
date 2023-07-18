# Kapitel 1: Objektorientierte Programmierung mit Python

## Themen

* Objektorientierte Programmierung
* Klassen
* Vererbung
* `__init__`-Methode
* `__del__`-Methode
* `__name__`-Attribut
* Design Patterns
  * Interface - Duck-Typing
  * Singleton - Modulansatz
  * Observer
* Exceptions
* Decorators

## Was wir programmieren

In diesem Kapitel werden wir einen Kaffeeautomaten programmieren, um die Konzepte der objektorientierten Programmierung in Python besser zu verstehen.

## Ablauf

1. Einführung in die objektorientierte Programmierung
   * Definition und Grundprinzipien der objektorientierten Programmierung
   * Vorteile und Anwendungsgebiete

2. Klassen
   * Einführung in Klassen und ihre Bedeutung in der objektorientierten Programmierung
   * Erstellung einer Klasse in Python
   * Verwendung von Standardwerten in Klassenattributen
   * Unterschiedliche Datentypen in Klassenattributen
   * Die `__init__`-Methode für die Initialisierung von Objekten
   * Die `__del__`-Methode für die Bereinigung von Objekten
   * Das `__name__`-Attribut zur Überprüfung des Namens einer Klasse

3. Vererbung
   * Einführung in das Konzept der Vererbung und seine Vorteile
   * Vererbungshierarchien und Klassendiagramme
   * Erstellung einer Hauptdatei (`main.py`) zur Veranschaulichung der Vererbung
   * Implementierung der Vererbung in Python mit Hilfe des Moduls `01_inheritance`

4. Interface - Duck-Typing
   * Verwendung des Moduls `abc` zur Erstellung von abstrakten Klassen und Methoden
   * Deklaration von abstrakten Methoden mit `pass`
   * Implementierung eines Interfaces mit dem Modul `02_interface`
   * Hinweis auf eine bekannte Problematik in bestimmten Python-IDEs

5. Observer
   * Einführung in das Observer-Design-Pattern
   * Veranschaulichung des Patterns mit einem Diagramm
   * Implementierung des Observer-Patterns in Python mit dem Modul `03_observer`

6. Exceptions
   * Überblick über Standard-Exceptions in Python
   * Erstellung eigener Exceptions
   * Verwendung der Python-Dokumentation für spezifische Exceptions
   * Hinweis auf das Modul `exceptions` und seine konkreten Exceptions

7. Lambda-Funktionen
   * Einführung in Lambda-Funktionen als anonyme Funktionen
   * Verwendung von Lambda-Funktionen zur vereinfachten Implementierung bestimmter Logiken
   * Beispielanwendung mit dem Modul `05_lambda_function`
   * Hinweis auf die Einhaltung von Flake8-Regeln für Lambda-Funktionen

8. Innere Funktionen
   * Nutzung von inneren Funktionen zur Strukturierung des Codes und Verbesserung der Lesbarkeit
   * Implementierung von inneren Funktionen in Python
   * Beispielanwendung mit dem Modul `06_inner_functions`

9. Decorators
   * Einführung in Decorators als Funktionen, die andere Funktionen modifizieren oder erweitern
   * Verwendung von Decorators zur Hinzufügung von Zusatzfunktionalität ohne direkte Änderung des Quellcodes
   * Implementierung von Decorators mit dem Modul `07_decorators`

10. Der Kaffee-Automat
    * Zusammenführung der erlernten Konzepte zur Implementierung eines Kaffeeautomaten in Python
    * Praktische Anwendung der objektorientierten Programmierung