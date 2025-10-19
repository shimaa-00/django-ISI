from django.db import models
from track.models import Track
from django.shortcuts import get_object_or_404
# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=20)
    faculty = models.CharField (max_length=50)
    image = models.ImageField(upload_to='student/' , null = True , blank=True)
    track = models.ForeignKey (Track , on_delete=models.CASCADE)
    age = models.IntegerField(null = True)
    @classmethod
    def get_student (cls , id ):
        student = get_object_or_404(cls , pk = id)
        return student 
    def __str__(self):
        return self.name
    