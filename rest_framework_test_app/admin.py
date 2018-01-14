from django.contrib import admin
from rest_framework_test_app.models import Company, Department, Employee

# Register your models here.

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)