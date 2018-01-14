from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_test_app import views as test_app_views


urlpatterns = [
    url(r'^company/$', test_app_views.CompanyList.as_view()),
    url(r'^company/(?P<pk>[0-9]+)/$', test_app_views.CompanyDetail.as_view()),
    url(r'^department/$', test_app_views.DepartmentList.as_view()),
    url(r'^department/(?P<pk>[0-9]+)/$', test_app_views.DepartmentDetail.as_view()),
    url(r'^employee/$', test_app_views.EmployeeList.as_view()),
    url(r'^employee/(?P<pk>[0-9]+)/$', test_app_views.EmployeeDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)