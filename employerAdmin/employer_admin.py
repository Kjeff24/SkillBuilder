from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'SkillBuilder Employer Administration'
    site_title = 'SkillBuilder Employer Administration'
    login_template = 'admin/login.html'

employer_admin_site = MyAdminSite(name='employer_admin')