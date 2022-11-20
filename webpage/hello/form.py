from django.forms import ModelForm
from .models import Courses, Program

class ProgramForm(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        