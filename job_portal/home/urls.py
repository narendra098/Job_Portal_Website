from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('userhome/',views.job_seeker,name='userhome'),
    path('emphome/',views.employee, name='emphome'),
    path('available_jobs',views.job_listing,name='job_listing'),
]