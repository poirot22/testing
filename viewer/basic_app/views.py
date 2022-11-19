from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import csv
from django.http import HttpResponse
# Create your views here.

class FacultyListView(ListView):
    model=models.Faculty

class FacultyDetailView(DetailView):
    model=models.Faculty
    template_name='basic_app/faculty.html'

class FacultyCreateView(CreateView):
    fields=('name','age','designation','gender','dob','faculty_id','blood_group','aadhar_no',
    'pan_no','mobile','email','state','district','pin','house_no','locality','permanent_address_is_same_as_current_address',
    'qualification','college','university','percentage','award','year_of_award','organisation_of_award',
    'publication_journal_name','publication_journal_vol','issn_no','publisher','year_of_publication','article_title',
    'project_title','duration','cost_of_project','funding_agency','start_date','end_date'
    )
    model=models.Faculty

class FacultyUpdateView(UpdateView):
    fields=('name','age','designation','gender','dob','faculty_id','blood_group','aadhar_no',
    'pan_no','mobile','email','state','district','pin','house_no','locality','permanent_address_is_same_as_current_address',
    'qualification','college','university','percentage','award','year_of_award','organisation_of_award',
    'publication_journal_name','publication_journal_vol','issn_no','publisher','year_of_publication','article_title',
    'project_title','duration','cost_of_project','funding_agency','start_date','end_date'
    )
    model=models.Faculty

class FacultyDeleteView(DeleteView):
    model=models.Faculty
    success_url=reverse_lazy('basic_app:list')



def searchbar(request):
    if request.method=='GET':
        search=request.GET.get('search')


        facs=models.Faculty.objects.all().filter(faculty_id=search)

        return render(request,'basic_app/searchbar.html',{'facs':facs})


'''def venue_pdf(request):
    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    lines=[]

    faculties=models.Faculty.objects.all()

    for faculty in faculties:
        lines.append(faculty.faculty_id)
        lines.append("Name:" + faculty.name)
        lines.append("Designation:" + faculty.designation)
        lines.append('--')


    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='faculty_report.pdf')'''


def faculty_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename=faculty.csv'

    writer=csv.writer(response)

    faculties=models.Faculty.objects.all()

    writer.writerow(['Name','ID','Designation','Age','Gender','Email','Mobile Number','DOB','Aadhar','PAN','State','District','PIN','House Number','Locality','Qualification','College',
                    'University','Percentage','Award','Year of Award','Organisation of Award','Publication Journal','Journal Volume','ISSN Number','Publisher','Year of Publication',
                    'Article Title','Project Title','Duration','Cost of Project','Funding Agency','Start Date','End Date'])



    for faculty in faculties:
        writer.writerow([faculty.name,faculty.faculty_id,faculty.designation,faculty.age,faculty.gender,faculty.email,faculty.mobile,faculty.dob,faculty.aadhar_no,
                        faculty.pan_no,faculty.state,faculty.district,faculty.pin,faculty.house_no,faculty.locality,faculty.qualification,faculty.college,faculty.university,
                        faculty.percentage,faculty.award,faculty.year_of_award,faculty.organisation_of_award,faculty.publication_journal_name,faculty.publication_journal_vol,
                        faculty.issn_no,faculty.publisher,faculty.year_of_publication,faculty.article_title,faculty.project_title,faculty.duration,faculty.cost_of_project,
                        faculty.funding_agency,faculty.start_date,faculty.end_date])

    return response


def home(request):
    return render(request,'basic_app/home.html')


'''def user_login (request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login (request, user)
                return render(request,'basic_app/faculties.html')
            else:
                return HttpResponse('user not active')
        else:
            return HttpResponse('User doesnt exist')
    else:
        return render(request,'login.html')'''


'''fields=('name','age','designation','gender','dob','faculty_id','blood_group','aadhar_no',
'pan_no','mobile','email','state','district','pin','house_no','locality','permanent_address_is_same_as_current_address',
'qualification','college','university','percentage','award','year_of_award','organisation_of_award',
'publication_journal_name','publication_journal_vol','issn_no','publisher','year_of_publication','article_title',
'project_title','duration','cost_of_project','funding_agency','start_date','end_date'
)'''
