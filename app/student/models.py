from app import db
from app.common

class Student(Base):
    def __init__(self, student_id, name):
        self.id = id
        self.name = name
        self.grade = grade

    __tablename__ = 'student'

    student_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(128), nullable=False)
