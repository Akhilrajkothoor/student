from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import student
from studentapp.models import Student
from . forms import StudentForm


def index(request):
    student=Student.objects.all()
    context={'student_list':student}
    return render(request,'index.html',context)
def detail(request,student_id):
    student=Student.objects.get(id=student_id)
    return render(request,"details.html",{'student':student})
def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        department = request.POST.get('department',)
        email = request.POST.get('email',)
        mobile = request.POST.get('mobile',)
        address = request.POST.get('address',)
        student=Student(name=name,department=department,email=email,mobile=mobile,address=address)
        student.save()

    return render(request,'add.html')

def update(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(request.POST or None,request.FILES,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'student':student})
def delete(request,id):
    if request.method=='POST':
        movie=Student.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
