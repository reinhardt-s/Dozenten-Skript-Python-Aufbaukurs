# Definieren Sie Film-, Schauspieler- und FilmSchauspieler-Tabellen mit SQLAlchemy.
# Die Filme sollen Titel und Veröffentlichungsjahr haben.
# Schauspieler sollen Vor- und Nachnamen haben.
# Die FilmSchauspieler-Tabelle soll eine n:n-Beziehung zwischen Filmen und Schauspielern darstellen.
# Fügen Sie einige Filme und Schauspieler in Ihre Datenbank ein.
# Vergessen Sie nicht, auch Einträge in Ihrer FilmSchauspieler-Tabelle zu machen, um die Beziehung darzustellen.
# Schreiben Sie Abfragen, um Folgendes zu tun:
# Ermitteln Sie alle Schauspieler in einem bestimmten Film.
# Finde alle Filme, in denen ein bestimmter Schauspieler aufgetreten ist.

# Schreiben Sie eine Abfrage, um den Film mit den meisten Schauspielern zu ermitteln.
# Verwende hierfür SQLAlchemy-Funktionen, um die Anzahl der Schauspieler für jeden Film zu zählen
# und dann den Film mit der höchsten Anzahl zu ermitteln.
# Schreibe eine Abfrage, um Schauspieler zu finden, die in mehr als einem Film aufgetreten sind.
# Diese Abfrage soll alle Schauspieler zurückgeben, die mehr als einen Eintrag in der FilmSchauspieler-Tabelle haben.
# Schreibe eine Abfrage, um Filme zu finden, die im selben Jahr veröffentlicht wurden.
# Diese Abfrage soll alle Filme gruppieren, die im selben Jahr veröffentlicht wurden,
# und die Anzahl der Filme für jedes Jahr ausgeben.
# Nutze hierfür:
# join() - Doku: https://docs.sqlalchemy.org/en/
# group_by()
# having()
# count()
# func()
# subquery()
# aliased()


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, func, select
from sqlalchemy.orm import relationship, Session, declarative_base, aliased

Base = declarative_base()
engine = create_engine('sqlite:///movies.db', echo=False)

# Datenbanktabelle löschen
meta = MetaData()
meta.reflect(bind=engine)
meta.drop_all(bind=engine)


association_table = Table('film_actor', Base.metadata,
                          Column('film_id', Integer, ForeignKey('films.id')),
                          Column('actor_id', Integer, ForeignKey('actors.id'))
                          )


class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_year = Column(Integer)
    actors = relationship("Actor", secondary=association_table, back_populates="films")


class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    films = relationship("Film", secondary=association_table, back_populates="actors")

Base.metadata.create_all(engine)
session = Session(engine)


actor1 = Actor(first_name="Robert", last_name="Downey Jr.")
actor2 = Actor(first_name="Chris", last_name="Evans")
film1 = Film(title="Iron Man", release_year=2008, actors=[actor1, actor2])
film2 = Film(title="The Avengers", release_year=2012, actors=[actor1, actor2])
film3 = Film(title="Avengers: Endgame", release_year=2019, actors=[actor1, actor2])
film4 = Film(title="Captain America: The First Avenger", release_year=2012, actors=[actor2])
film5 = Film(title="Captain America: Civil War", release_year=2016, actors=[actor2])
session.add(actor1)
session.add(actor2)
session.add(film1)
session.commit()




# Der Film mit den meisten Schauspielern
most_actors = select(Film.title, func.count('*').label('actor_count')).\
    join(association_table).\
    group_by(Film.title).\
    order_by(func.count('*').desc())
result_set = session.scalars(most_actors).first()

print(result_set)

# Schauspieler, die in mehr als einem Film aufgetreten sind
actors_in_multiple_films = select(Actor.first_name, Actor.last_name, func.count('*').label('film_count')).\
    join(association_table).\
    group_by(Actor.id).\
    having(func.count('*') > 1)
result_set = session.scalars(actors_in_multiple_films).all()
print(result_set)

# Filme, die im selben Jahr veröffentlicht wurden

# Abgeleitete Tabelle, die die Jahre und die Anzahl der Filme in diesen Jahren enthält
film_counts = select(Film.release_year, func.count('*').label('film_count')).\
    group_by(Film.release_year).\
    having(func.count('*') > 1).\
    subquery()

# Alias für die Film-Klasse
FilmAlias = aliased(Film)

# Abfrage zur Abrufung der Filme, die in den Jahren veröffentlicht wurden,
# die in der ersten Abfrage zurückgegeben wurden
films_same_year = select(FilmAlias).\
    join(film_counts, FilmAlias.release_year == film_counts.c.release_year).\
    order_by(FilmAlias.release_year, FilmAlias.title)
films_same_year = session.scalars(films_same_year).all()

# Ergebnisse ausgeben
for film in films_same_year:
    print(f"Titel: {film.title}, Veröffentlichungsjahr: {film.release_year}")


