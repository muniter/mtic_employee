from sqlalchemy import Column, ForeignKey, Integer, Float, String, Text, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declared_attr
from mtapp.db import Base
from mtapp.enums import GenderEnum, ContractEnum

class Record:
    model = "record"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    edited_at = Column(DateTime, nullable=False)

    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey('user.id'), nullable=False)

    @declared_attr
    def edited_by(cls):
        return Column(Integer, ForeignKey('user.id'), nullable=False)

    @declared_attr
    def deleted_by(cls):
        return Column(Integer, ForeignKey('user.id'), nullable=False)

    @declared_attr
    def owner(cls):
        return Column(Integer, ForeignKey('user.id'), nullable=False)

    @declared_attr
    def group(cls):
        return Column(Integer, ForeignKey('group.id'), nullable=False)


    def read(self):
        pass

    def write(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def __repr__(self):
        return f'<{self.model} {self.name!r}>'

class User(Record, Base):
    model = 'user'
    __tablename__ = model
    # Must sync with employee.email
    username = Column(String(120), unique=True, nullable=False)
    # TODO: Hash this
    password = Column(String, nullable=False)

    def login(self):
        pass

    def __repr__(self):
        return f'<{self.model} {self.name!r}>'

class Group(Record, Base):
    model = 'group'
    __tablename__ = model
    name = Column(String(120), unique=True, nullable=False)
    perm_level = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<{self.model} {self.name!r}>'

class Employee(Record, Base):
    model = "employee"
    __tablename__ = model
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String)
    gender = Enum(GenderEnum)
    joined_at = Column(DateTime)
    gender = Enum(ContractEnum)
    job_title = Column(String(120))
    dependency = Column(String(120))
    salary = Column(Float)

    def __repr__(self):
        return f'<{self.model} {self.name!r}>'


# TODO: Useful code for backreffing an object
# category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
#     nullable=False)
# category = db.relationship('Category',
#     backref=db.backref('posts', lazy=True))
