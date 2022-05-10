from django.shortcuts import render
import requests
from home.models import Website_Users

# Create your views here.
def postjobpage(request):
    if request.method=='POST':
        job_name = request.POST['job_name']
        company = request.POST['company']
        empname = request.POST['emp_name']
        empmail = request.POST['empmail']
        desc = request.POST['desc']
        print(job_name)

        url = 'http://127.0.0.1:8000/add_job'
        data = {
        'job_name':job_name,
        'company': company,
        'empname': empname,
        'empmail':empmail,
        'desc': desc,
        }
        r = requests.post(url,data=data)

    return render(request, 'post_job.html')

def posted_jobs(request):
    api_url = 'http://127.0.0.1:8000/view_jobs'
    jobs = requests.get(api_url)
    data = jobs.json()
    curr_user = request.user
    userobj=Website_Users.objects.get(user_name=curr_user)
    print(curr_user)
    return render(request,'posted_jobs.html',{'data':data,'user_mail':userobj.mail})