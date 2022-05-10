from django.urls import path
from . import views
  
urlpatterns = [
  path('postjob',views.postjobpage,name='addjob'),
  path('posted_jobs',views.posted_jobs,name='posted_jobs'),
   ]