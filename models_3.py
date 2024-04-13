from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'Студент ({self.firstname}, {self.lastname}, {self.score})'


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    namelesson = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    student = db.relationship('Student', backref=db.backref('score'), lazy=True)
    
    def __repr__(self):
        return f'{self.score}'