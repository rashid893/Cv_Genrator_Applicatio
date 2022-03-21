from lib2to3.pytree import LeafPattern
import profile
from urllib import response
from click import option
from django.shortcuts import render,HttpResponse
from .models import Profile
import pdfkit
from django.template import loader

# Create your views here.
def index(request):
    msg= "Your Form SuccessFully Submited"
    if request.method =="POST":
        # name=request.POST.get("name","")
        # email=request.POST.get("email","")
        # phone=request.POST.get("phone","")
        # summary=request.POST.get("summary","")
        # degree=request.POST.get("degree","")
        # school=request.POST.get("school","")
        # university=request.POST.get("university","")
        # previous=request.POST.get("previous","")
        # skills=request.POST.get("skills","")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        summary=request.POST['summary']
        degree=request.POST['degree']
        school=request.POST['school']
        university=request.POST['university']
        previous=request.POST['previous']
        skills=request.POST['skills']
        
        ids=Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous=previous,skills=skills)
        ids.save()
        
       
    return render(request,"index.html",{'msg':msg})
def resume(request,id):
    userp=Profile.objects.get(pk=id)
    template=loader.get_template('reusme.html')
    html=template.render({'userp':userp})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Dispostion']='attachment'
    filename="resume.pd"
    return response
def list(request):
    profile=Profile.objects.all()


    return render(request,'list.html',{'profile':profile})
