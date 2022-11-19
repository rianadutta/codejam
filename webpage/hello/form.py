from django.forms import ModelForm
from .models import Courses

class ProgramForm(ModelForm):
    class Meta:
        model = Coursesfields = '__all__'