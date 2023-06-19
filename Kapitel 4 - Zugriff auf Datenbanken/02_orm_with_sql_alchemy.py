from prettytable import PrettyTable
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, MetaData, select
from sqlalchemy.orm import Session, declarative_base, relationship

# Erzeugt ein neues Basisklasse-Objekt,
# das als gemeinsame Basis für alle Modelle dient, die von ihm ableiten.
Base = declarative_base()

# Verbindung aufbauen
engine = create_engine('sqlite:///etc.db', echo=False)

# Datenbanktabelle löschen
meta = MetaData()
meta.reflect(bind=engine)
meta.drop_all(bind=engine)


# Datenbanktabelle erstellen
class User(Base):
    # Tabellenname
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)


# Datenbanktabelle erstellen, welche noch nicht existieren
Base.metadata.create_all(engine)

# Einträge hinzufügen

# Session erstellen
session = Session(engine)


def create_user(name, email):
    user = User(user_name=name, email=email)
    session.add(user)
    session.commit()


def print_all_users():
    table = PrettyTable(['ID', 'Name', 'Email'])
    users = session.query(User).all()
    for user in users:
        table.add_row([user.id, user.user_name, user.email])

    print(table)


def update_user(name, new_name):
    user = get_user_by_name(name)
    user.user_name = new_name
    session.commit()


def delete_user(name):
    user = get_user_by_name(name)
    session.delete(user)
    session.commit()


def get_user_by_name(name):
    user = select(User).filter_by(user_name=name)
    result_set = session.scalars(user).one()
    return result_set


# Create
create_user('Alex Stone', 'a_atone@etc.at')
create_user('Joe Smith', 'j_smith@etc.at')
create_user('Alice Bree', 'a_bree@etc.at')

# Query
print_all_users()

# Update
update_user('Alex Stone', 'Riley Stone')
print_all_users()

# Delete
delete_user('Joe Smith')
print_all_users()

# Close
session.close()


class Course(Base):
    # Tabellenname
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    description = Column(String)


def create_course(name, description):
    course = Course(course_name=name, description=description)
    session.add(course)
    session.commit()


def get_course_by_name(name):
    course = select(Course).filter_by(course_name=name)
    result_set = session.scalars(course).one()
    return result_set


class Booking(Base):
    # Tabellenname
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(column=User.id))
    course_id = Column(Integer, ForeignKey(column=Course.id))

    user = relationship("User", backref="bookings")  # Relationship zur User Tabelle
    course = relationship("Course", backref="bookings")


def create_booking(user_id, course_id):
    booking = Booking(user_id=user_id, course_id=course_id)
    session.add(booking)
    session.commit()


def print_all_courses():
    table = PrettyTable(['Name', 'Description'])
    courses = select(Course)
    result_set = session.scalars(courses).all()
    for course in result_set:
        table.add_row([course.course_name, course.description])

    print(table)


def print_all_bookings():
    table = PrettyTable(['User', 'Course'])
    bookings = select(Booking)
    result_set = session.scalars(bookings).all()
    for booking in result_set:
        table.add_row([booking.user_id, booking.course_id])

    print(table)


# Datenbanktabelle erstellen, welche noch nicht existieren
Base.metadata.create_all(engine)

# Einträge hinzufügen
create_course('Python', 'Python for Beginners')
create_course('Java', 'Java for Beginners')
create_course('C++', 'C++ for Beginners')

create_booking(get_user_by_name('Riley Stone').id, get_course_by_name('Python').id)
create_booking(get_user_by_name('Riley Stone').id, get_course_by_name('Java').id)
create_booking(get_user_by_name('Riley Stone').id, get_course_by_name('C++').id)

create_booking(get_user_by_name('Alice Bree').id, get_course_by_name('Python').id)


def print_all_bookings_for_user(user_name):
    table = PrettyTable(['User', 'Course'])
    #
    # Nutzt JOIN um die Daten aus der Tabelle Booking, User und Course zu verbinden
    bookings = select(Booking).join(User).join(Course).filter(User.user_name == user_name)
    result_set = session.scalars(bookings).all()
    for booking in result_set:
        table.add_row([booking.user.user_name, booking.course.course_name])

    print(table)


print_all_bookings_for_user('Riley Stone')
