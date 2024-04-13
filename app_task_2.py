# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template
from models_2 import db, Author, Book
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase2.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for author in range(1, 4):
        new_author = Author(firstname=f'{author}', lastname=f'{author}')
        db.session.add(new_author)
    db.session.commit()

    for book in range(1, 11):
        for i in range(1, 4):
            new_book = Book(name=f'Название книги {book}', year = random.randint(1900, 2000), quantity = random.randint(1, 9999), id_author=i)
            db.session.add(new_book)
    db.session.commit()


@app.route('/books/')
def get_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)




if __name__ == '__main__':
    app.run(debug=True)