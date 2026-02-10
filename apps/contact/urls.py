from django.urls import path
from apps.contact.views import contact_page



urlpatterns = [ 
    path('contact/', contact_page, name='contact_page'), 
    
]
