from django.urls import path
from apps.about.views import employeeFunc, employee_detail, about


urlpatterns = [ 
    path('about/', about, name='about'),
    path('employee/', employeeFunc, name='employeeFunc'),
    path('employee/<slug:slug>/', employee_detail, name='employee_detail'), 
]

