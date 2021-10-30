from flask_appbuilder.models.sqla.filters import FilterEqual, FilterNotEqual
from .filters import FilterNotEqualsIfAdmin
from flask_appbuilder.security.views import UserDBModelView

class MyUserDBModelView(UserDBModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """

    base_filters = [['is_sudo', FilterNotEqualsIfAdmin, True]]
    add_form_query_rel_fields = {'roles': [['name', FilterNotEqualsIfAdmin, 'Sudo']]}
    edit_form_query_rel_fields = add_form_query_rel_fields
    show_fieldsets = [
        ('User info',
         {'fields': ['username', 'active', 'roles', 'login_count', 'employee']}),
        ('Personal Info',
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        ('Audit Info',
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        ('User info',
         {'fields': ['username', 'active', 'roles', 'login_count', 'employee']}),
        ('Personal Info',
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    add_columns = [
        'first_name',
        'last_name',
        'username',
        'active',
        'email',
        'roles',
        'employee',
        'password',
        'conf_password'
    ]
    list_columns = [
        'first_name',
        'last_name',
        'username',
        'employee',
        'active',
        'roles'
    ]
    edit_columns = [
        'first_name',
        'last_name',
        'username',
        'active',
        'email',
        'roles',
        'employee',
    ]
