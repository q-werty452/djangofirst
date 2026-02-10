from django.urls import path
from apps.news.views import homepage, news_detail, category_detail, search, profile, registr
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('', homepage, name='homepage'), 
    path('search/', search, name='search'), 
    path('news/<slug:slug>/', news_detail, name='news_detail'), 
    path('category/<slug:slug>/', category_detail, name='category_detail'),

    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),


    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registr/', registr, name='registr'),

]
# # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('registr/', registr, name='registr'),path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('registr/', registr, name='registr'),