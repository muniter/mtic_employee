import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Boolean, Date, ForeignKey, Integer, Float, String, Text, Enum
from flask_appbuilder.security.sqla.models import User
# from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from .enums import GenderEnum, ContractEnum

class Record:
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Record, Model):
    __tablename__ = "department"
    comment = Column(String(50), unique=False, nullable=False)

class JobTitle(Record, Model):
    __tablename__ = "jobtitle"
    name = Column(String(50), unique=True, nullable=False)

class Employee(Record, Model):
    __tablename__ = "employee"
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String)
    gender = Column(Enum(GenderEnum))
    joined_at = Column(Date)
    left_at = Column(Date)
    contract = Column(Enum(ContractEnum))
    contract_start = Column(Date)
    contract_end = Column(Date)
    jobtitle_id = Column(Integer, ForeignKey("jobtitle.id"), nullable=False)
    jobtitle = relationship("JobTitle")
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    department = relationship("Department")
    salary = Column(Float)
    reports = relationship("EmployeeReport", backref="employee")

class MyUser(User):
    __tablename__ = "ab_user"
    employee_id = Column(Integer, ForeignKey("employee.id"), nullable=True)
    employee = relationship("Employee", backref="user")
    is_sudo = Column(Boolean, default=False)

class EmployeeReport(Record, Model):
    __tablename__ = "employeereport"
    name = Column(String, unique=False, nullable=False)
    text = Column(Text, nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"))
