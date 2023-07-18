# Definiere die Funktion send_confirmations_to_trainee:
# Es soll versuche werden, für jeden Trainee den hinterlegten Kurs zu buchen.
# Ist dies erfolgreich, ruft die Funktion booked(course_name) auf und gibt True zurück.
# Sollte dieser Kurs nicht angeboten werden, soll stattdessen 'Python - Einführung für Programmierer' gebucht,
# changed_course aufgerufen und False zurückgegeben werden
# Schlussendlich soll nach jedem Buchungsversuch send_info_to_staff() aufgerufen werden

from no_such_course_exception import NoSuchCourseException
from pc_college import PcCollege
from trainee import Trainee

pc_college = PcCollege()
trainees = [
    Trainee(name="Alex", course="Microsoft Teams - Grundlagen Seminar", skill_points=44),
    Trainee(name="Alice", course="Python Aufbaukurs", skill_points=12),
    Trainee(name="Bob", course="MySQL - SQL Grundlagen"),
]

failed_bookings = 0


def booked(course_name: str) -> None:
    """
    Prints a message indicating that the course was successfully booked.
    :param course_name: The name of the course that was booked.
    """
    print(f'Sende... Der Kurs {course_name} konnte erfolgreich gebucht werden.')


def changed_course() -> None:
    """
    Prints a message indicating that the desired course is not available and that "Python - Einführung für Programmierer"
    will be booked instead.
    """
    print('Sende... Der gewünschte Kurs ist nicht verfügbar. Stattdessen wird "Python - Einführung für '
          'Programmierer" gebucht.')


def send_info_to_staff() -> None:
    """
    Prints a message indicating that another course has been booked through the API.
    """
    print('Ein weiterer Kurs wurde über unsere API gebucht.')


def send_confirmations_to_trainee(current_trainee: Trainee) -> bool:
    """
    Attempts to book the desired course for the given trainee. If the course is not available, books "Python - Einführung
    für Programmierer" instead and returns False.
    :param current_trainee: The trainee who wants to attend the course.
    :return: True if the booking was successful, False if "Python - Einführung für Programmierer" was booked instead.
    """
    try:
        pc_college.book_course(current_trainee.course)
        booked(current_trainee.course)
        return True
    except NoSuchCourseException:
        pc_college.book_course('Python - Einführung für Programmierer')
        changed_course()
        return False
    finally:
        send_info_to_staff()


for trainee in trainees:
    if not send_confirmations_to_trainee(trainee):
        failed_bookings += 1

print(f'Es ist/sind {failed_bookings} Buchung(en) fehlgeschlagen.')



for trainee in trainees:
    if not send_confirmations_to_trainee(trainee):
        failed_bookings += 1

print(f'Es ist/sind {failed_bookings} Buchung(en) fehlgeschlagen.')
