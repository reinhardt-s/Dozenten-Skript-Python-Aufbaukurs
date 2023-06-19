# Verbinden Sie sich mit einer lokalen SQLite-Datenbank und
# erstellen Sie eine Tabelle für "Books" mit den Feldern "id", "title" und "author".
# "Authors" soll eine Tabelle mit den Feldern "id" und "name" sein.
# Fügen Sie einige Bücher zur Tabelle hinzu und führen Sie Abfragen durch, um die Bücherliste zu erhalten.

from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, select
from sqlalchemy.orm import relationship, declarative_base, Session

Base = declarative_base()
engine = create_engine('sqlite:///library.db', echo=False)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')

Base.metadata.create_all(engine)
session = Session(engine)

# Insert data
author1 = Author(name='Stephen King')
author2 = Author(name='J. K. Rowling')
book1 = Book(title='The Shining', author=author1)
book2 = Book(title='Harry Potter', author=author2)

session.add(book1)
session.add(book2)
session.add(author1)
session.add(author2)
session.commit()

# Query data
books = select(Book)
result_set = session.scalars(books)
for book in result_set:
    print(book.title, book.author.name)