from django.urls import path
from . import views


urlpatterns = [
   #for api's
   path('add_job',views.PostJob.as_view()),
   path('view_jobs',views.ViewJobs.as_view()),
   path('job/<int:pk>',views.JobRetrive.as_view()),
   path('update_job/<int:pk>',views.UpdateJob.as_view()),
   
 
]