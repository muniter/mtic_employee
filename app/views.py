from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from . import appbuilder, db
from .models import Department, JobTitle, Employee, EmployeeReport 


def department_query():
    return db.session.query(Department)


class EmployeeReportView(ModelView):
    datamodel = SQLAInterface(EmployeeReport)
    # add_columns = ["name"]
    # edit_columns = ["name"]
    # show_columns = ["name"]
    list_columns = ["name", "employee"]


class EmployeeView(ModelView): 
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

# appbuilder.add_view_no_menu(EmployeeHistoryView, "EmployeeHistoryView")
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
