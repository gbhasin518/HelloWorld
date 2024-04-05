from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    major_id = db.Column(db.Integer, db.ForeignKey('major.major_id'))
    birth_date = db.Column(db.DateTime, nullable=False)
    num_credits_completed = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    is_honors = db.Column(db.Boolean, nullable=False)

    def __init__(self, first_name, last_name, major_id, birth_date, is_honors):
        self.first_name = first_name
        self.last_name = last_name
        self.major_id = major_id
        self.birth_date = birth_date
        self.num_credits_completed = 0
        self.gpa = 0.0
        self.is_honors = is_honors

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Major(db.Model):
    __tablename__ = "major"

    major_id = db.Column(db.Integer, primary_key=True)
    major = db.Column(db.String(30), nullable=False)
    students = db.relationship('Student', backref='students')

    def __init__(self, major):
        self.major = major

    def __repr__(self):
        return f"{self.major}"

class Email(db.Model):
    __tablename__ = "email"

    email_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), unique=True)  # This ensures one-to-one relation

    student = db.relationship('Student', backref=db.backref('email', uselist=False, lazy=True))

    def __init__(self, email, student_id):  # You should pass the student_id as well
        self.email = email
        self.student_id = student_id

    def __repr__(self):
        return f"<Email {self.email}>"
