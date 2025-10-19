from django.shortcuts import render , redirect , get_object_or_404
from track.models import Track
from .models import Student
from .forms import Student_create
# Create your views here.
def student_index(request):
    students = Student.objects.all()
    return render (request, 'student/index.html' , {"students" : students})
def show_student_details(request , id ):
    student = Student.get_student(id)
    if student :
        return render(request , 'student/student_details.html' , {"student":student})
def student_delete (request , id):
    student = Student.get_student(id)
    if (student):
        student.delete()
    return redirect (student_index)
def create_student (request):
    tracks = Track.objects.all()
    if request.method == "GET":
        return render (request , 'student/create_student.html' , {"tracks":tracks})
    elif request.method == "POST" :
        print (request.POST)
        name = request.POST['name']
        age = int (request.POST['age'])
        faculty = request.POST['faculty']
        track_id = request.POST['track']
        image  = request.FILES['image']

        if  (3 <= len(name) <=20 )and (age >=18): 
            new_student = Student()
            new_student.name = name 
            new_student.age = age
            new_student.faculty= faculty
            new_student.track=Track.objects.get (pk = track_id)
            new_student.image = image
            new_student.save()
            return redirect (student_index)
        else :
            context = {"errors" : 'name must be at least 3 characters , age must be +18'}
            context["tracks"] = tracks
            return render (request , 'student/create_student.html' , context)

       
def create_student (request):
    form = Student_create()
    if request.method == "GET":
        return render (request , 'student/create_student.html' , {"form" : form})
    elif request.method == "POST":
        form_data = Student_create(request.POST , request.FILES)
        if form_data.is_valid():
            new_student = Student()
            new_student.name = form_data.cleaned_data["name"]
            new_student.age = form_data.cleaned_data["age"]
            new_student.faculty = form_data.cleaned_data["faculty"]
            new_student.image = form_data.cleaned_data["image"]
            new_student.track = Track.objects.get (pk = form_data.cleaned_data['track'])
            new_student.save()
            return redirect (student_index)
        else:
            context = {"errors" : 'name must be at least 3 characters , age must be +18'}
            context["tracks"] = Track.objects.all()
            context["form"] = form
            return render (request , 'student/create_student.html' , context)