from datetime import datetime
from random import randint as rint
from flask_appbuilder.cli import create_admin, create_user
from flask import current_app
import logging
import random

from app import db
from flask_appbuilder.security.sqla.models import User
from app.models import Department, JobTitle, Employee, EmployeeReport 

log = logging.getLogger(__name__)

roles = {
    "User": current_app.appbuilder.sm.find_role("User"),
    "Admin": current_app.appbuilder.sm.find_role("Admin"),
    "Sudo": current_app.appbuilder.sm.find_role(
        current_app.appbuilder.sm.auth_role_admin
    ),
}

def get_random_name(names_list, size=1):
    name_lst = [
        names_list[random.randrange(0, len(names_list))].decode("utf-8").capitalize()
        for _ in range(0, size)
    ]
    return " ".join(name_lst)

months = ["Enero", "Febrero", "Marzo", "Abril", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
text = [
    "El comportamiento y rendimiento en este periodo de fue muy satisfactorio",
    "El rendimiento en este periodo de estuvo muy por debajo del promedio",
]

def gen_report(employee):
    rmonth = months[rint(0, len(months) - 1)] + " 2021"
    rtext = text[rint(0, len(text) - 1)]
    return EmployeeReport(
        name = rmonth,
        text = rtext,
        employee_id = employee.id
    )


deps = [
    Department(name="Compras", comment="Encargado de compras"),
    Department(name="Ventas", comment="Encargado de ventas"),
    Department(name="TI", comment="Encargado de Tecnologías de Comunicación"),
]

titles = [
    JobTitle(name="Asesor Comercial"),
    JobTitle(name="Jefe Departamento"),
    JobTitle(name="Jefe de TI"),
]


def randdate():
    return datetime(rint(2019,2021), rint(1,12), rint(1,28))

def randdatetime():
    return datetime(rint(2019,2021), rint(1,12), rint(1,28), rint(1,12), rint(0,59))

def salary():
    return random.randrange(1000000, 5000000)

try:
    # Cleanup
    db.session.query(User).delete()
    db.session.query(Employee).delete()
    db.session.query(EmployeeReport).delete()
    db.session.query(JobTitle).delete()
    db.session.query(Department).delete()
    # Super Admin
    user = current_app.appbuilder.sm.add_user(
        "admin", "admin", "admin", "admin@admin.com", roles["Sudo"], "admin"
    )
    # Admin
    user = current_app.appbuilder.sm.add_user(
        "javier", "Javier", "López", "javier@ibarra.com", roles["Admin"], "admin"
    )
    db.session.commit()
except Exception:
    db.session.rollback()

try:
    [db.session.add(d) for d in deps]
    [db.session.add(s) for s in titles]
    db.session.commit()
except Exception as e:
    log.error("Creating Commits: %s", e)
    db.session.rollback()


f = open("resources/NAMES.DIC", "rb")
names_list = [x.strip() for x in f.readlines()]

f.close()
gender = ["Male", "Female"]

for i in range(1, 20):
    e = Employee()
    e.first_name = get_random_name(names_list, random.randrange(1, 2))
    e.last_name = get_random_name(names_list, random.randrange(1, 2))
    e.name = e.first_name + " " + e.last_name
    e.email = (e.first_name + e.last_name + "@.ibarra.org").lower()
    e.address = "Calle " + get_random_name(names_list) + " Carrera " + get_random_name(names_list)
    e.gender = "male" if i % 2 == 0 else "female"
    e.joined_at = randdate()
    e.left_at = randdate() if i % 2 == 0 else None
    e.contract = "indefinete" if i % 2 == 0 else "services"
    e.contract_start = randdate()
    e.contract_end = randdate()
    e.jobtitle_id = rint(1,3)
    e.department_id = rint(1,3)
    e.salary = salary()
    db.session.add(e)
    try:
        db.session.commit()
        print("inserted", e)
    except Exception as e:
        log.error("Creating Contact: %s", e)
        db.session.rollback()

employees = db.session.query(Employee)
i = 1
for employee in employees:
    if i == 1:
        username = "user"
        password = "admin"
    else:
        username = employee.email
        password = "password"

    for i in range(0, 4):
        report = gen_report(employee)
        db.session.add(report)

    user = current_app.appbuilder.sm.add_user(
        username, employee.first_name, employee.last_name, employee.email, roles["User"], password
    )
    user.employee_id = employee.id
    i += 1

db.session.commit()
