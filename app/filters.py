from flask import g, current_app
from flask_appbuilder.models.sqla.filters import BaseFilter, get_field_setup_query, set_value_to_type

user_role = None
def get_user_role():
    global user_role
    if user_role == None:
        user_role = current_app.appbuilder.sm.find_role("User")
    return user_role

admin_role = None
def get_admin_role():
    global admin_role
    if admin_role == None:
        admin_role = current_app.appbuilder.sm.find_role("Admin")
    return admin_role

sudo_role = None
def get_sudo_role():
    global sudo_role
    if sudo_role == None:
        sudo_role = current_app.appbuilder.sm.find_role("Sudo")
    return sudo_role

def has_role(user, role):
 return user.roles[0].id == role.id

class FilterEqualFunctionUser(BaseFilter):
    name = "Filter view with a function only if current user role is User"
    arg_name = "eqf"

    def apply(self, query, func):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        if has_role(g.user, get_user_role()):
            return query.filter(field == func())
        return query

class FilterEqualAdmin(BaseFilter):
    name = "Equal to, only applied if admin role"
    arg_name = "eq"

    def apply(self, query, value):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        value = set_value_to_type(self.datamodel, self.column_name, value)

        if has_role(g.user, get_admin_role()):
            return query.filter(field == value)
        return query
