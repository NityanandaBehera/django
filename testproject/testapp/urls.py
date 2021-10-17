from django.conf.urls import url
from testapp import views
urlpatterns = [
    url('contact',views.contact),
    url('hello',views.greeting),
    url('^$',views.home),
    url('employee',views.employee_info_view)
]
