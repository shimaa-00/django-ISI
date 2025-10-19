from django import forms
from track.models import Track
class Student_create (forms.Form):
    # [(1 , "os") , (2 , "sw"),(3, "AI")]
    tracks = Track.objects.all()
    choices = []
    for track in tracks :
        choices.append((track.id , track.name))
    name = forms.CharField (required= True , min_length= 3 , max_length=20 , label= "Name")
    age = forms.IntegerField(required=True )
    faculty = forms.CharField()
    image = forms.FileField ()
    track = forms.ChoiceField(choices=choices )
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18 :
            raise forms.ValidationError("age must be at least 18")
        return age 
    
