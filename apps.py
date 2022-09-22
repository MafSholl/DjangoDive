from django.contrib.admin.apps import AdminConfig

class PycharmDjangoAdminConfig(AdminConfig):
    default_site = 'admin.PycharmDjangoAdminSite'
