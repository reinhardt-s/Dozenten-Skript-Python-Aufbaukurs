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


def booked(course_name):
    print(f'Sende... Der Kurs {course_name} konnte erfolgreich gebucht werden.')


def changed_course():
    print('Sende... Der gewünschte Kurs ist nicht verfügbar. Stattdessen wird "Python - Einführung für '
          'Programmierer" gebucht.')


def send_info_to_staff():
    print('Ein weiterer Kurs wurde über unsere API gebucht.')


def send_confirmations_to_trainee(current_trainee) -> bool:
    """
    Versucht den gewünschten Kurs zu buchen.
    :param current_trainee: Trainee, welche*r am Kurs teilnehmen will.
    :return: True, wenn Buchung erfolgreich, False, wenn anderer Kurs stattdessen gebucht wurde.
    """
    # try:
    #     pc_college.book_course(current_trainee.course)
    # except NoSuchCourseException:
    #     pc_college.book_course('Python - Einführung für Programmierer')
    #     changed_course()
    #     return False
    # else:
    #     booked(current_trainee.course)
    #     return True
    # finally:
    #     send_info_to_staff()


for trainee in trainees:
    if not send_confirmations_to_trainee(trainee):
        failed_bookings += 1

print(f'Es ist/sind {failed_bookings} Buchung(en) fehlgeschlagen.')
