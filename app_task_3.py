# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, render_template
from models_3 import db, Student, Score
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase3.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for i in range(1, 9):
            new_score = Score(score=f'Оценка {random.randint(1, 5)}', namelesson= f'{random.choice(["математика", "физика", "химия"])}', id_student=i)
            db.session.add(new_score)
    db.session.commit()

    for student in range(1, 9):
        new_student = Student(firstname=f'Имя студента {student}', lastname=f'Фамилия студента {student}', group=str(random.randint(1, 100)), email = str({student}) + '@mail.ru')
        db.session.add(new_student)
    db.session.commit()


@app.route('/scores/')
def get_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('scores.html', **context)




if __name__ == '__main__':
    app.run(debug=True)