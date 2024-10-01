from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Contains definitions of tables and associated schema constructs
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define the Employee model
class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f'<Employee id={self.id}, name="{self.name}", salary={self.salary}>'

# Define the Department model
class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Department id={self.id}, name="{self.name}", location="{self.location}">'
