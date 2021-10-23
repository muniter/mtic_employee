from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User

class MyUser(User):
    __tablename__ = "ab_user"
    employee_id = Column(Integer, nullable=True)

