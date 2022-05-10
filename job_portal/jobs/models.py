from django.db import models

# Create your models here.cla
class Jobs(models.Model):
    job_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    empname = models.CharField(max_length=50,blank=True)
    empmail = models.EmailField(max_length=50,blank=True, null=True)
    desc = models.TextField(max_length=5000)
    status = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.job_name
    
