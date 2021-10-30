from flask import g, current_app
from flask_appbuilder.models.sqla.filters import BaseFilter, get_field_setup_query, set_value_to_type

roles = {
    "Sudo": False,
    "Admin": False,
    "User": False,
}

def get_role(name):
    role = roles[name]
    if not role:
        role = current_app.appbuilder.sm.find_role(name)
        roles[name] = role
    return role

def has_role(user, role):
    id = role.id
    for r in user.roles:
        if r.id == id:
            return True
    return False

class FilterEqualFunctionUser(BaseFilter):
    name = "Filter view with a function only if current user role is User"
    arg_name = "eqf"

    def apply(self, query, func):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        if has_role(g.user, get_role("User")):
            return query.filter(field == func())
        return query

class FilterNotEqualsIfAdmin(BaseFilter):
    name = "Not equals to, only applied if user has admin role"
    arg_name = "eq"

    def apply(self, query, value):
        query, field = get_field_setup_query(query, self.model, self.column_name)
        value = set_value_to_type(self.datamodel, self.column_name, value)

        if has_role(g.user, get_role("Admin")):
            return query.filter(field != value)
        return query
