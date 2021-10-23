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

class FilterEqualFunctionUser(BaseFilter):
    name = "Filter view with a function only if role is User"
    arg_name = "eqf"

    def apply(self, query, func):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        if g.user.roles[0].id == get_user_role().id:
            return query.filter(field == func())
        return query

class FilterEqualAdmin(BaseFilter):
    name = "Equal to only for Admin"
    arg_name = "eq"

    def apply(self, query, value):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        value = set_value_to_type(self.datamodel, self.column_name, value)

        if g.user.roles[0].id == get_admin_role().id:
            return query.filter(field == value)
        return query
