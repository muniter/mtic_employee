from flask import g
from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .filters import FilterEqualFunctionUser

from . import appbuilder, db
from .models import Department, JobTitle, Employee, EmployeeReport 


def get_user_employee_id():
    return g.user.employee_id

def get_user():
    return g.user

def department_query():
    return db.session.query(Department)

class EmployeeReportView(ModelView):
    base_filters = [['employee_id', FilterEqualFunctionUser, get_user_employee_id]]
    datamodel = SQLAInterface(EmployeeReport)
    list_columns = ["name", "employee"]


class EmployeeView(ModelView): 
    base_filters = [['id', FilterEqualFunctionUser, get_user_employee_id]]
    datamodel = SQLAInterface(Employee)
    list_columns = ["name", "department.name", "jobtitle.name"]
    edit_form_extra_fields = {
        "department": QuerySelectField(
            "Department",
            query_factory=department_query,
            widget=Select2Widget(extra_classes="readonly"),
        )
    }
    related_views = [EmployeeReportView]


class JobTitleView(ModelView):
    datamodel = SQLAInterface(JobTitle)
    list_columns = ["name"]
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


db.create_all()

appbuilder.add_view(
    EmployeeView, "Employees", icon="fa-folder-open-o", category="Company"
)
appbuilder.add_separator("Company")
appbuilder.add_view(
    DepartmentView, "Departments", icon="fa-folder-open-o", category="Company"
)
appbuilder.add_view(
    JobTitleView, "Job Title", icon="fa-folder-open-o", category="Company"
)
appbuilder.add_view(
    EmployeeReportView, "Employee Reports", icon="fa-folder-open-o", category="Company"
)
