from django.urls import path , include
from .views import *
urlpatterns = [
    path('' , student_index , name = "students"),
    path ('show/<id>' , show_student_details , name="student_details"), 
    path ('delete/<id>' ,student_delete, name="student_delete"), 
    path('create' , create_student , name='create_student'),
]
