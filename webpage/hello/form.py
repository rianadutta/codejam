from django import forms
from .models import Program

PROGRAM_CHOICES = [
    ('math_comp', 'Joint Mathematics & Computer Science'),
    ('math_comp_hon', 'Joint Honours Mathematics & Computer Science'),
    ('math', 'Mathematics')
]
class UserForm(forms.Form):
    program = forms.CharField(label="What program are you in?", required=True, widget=forms.Select(choices=PROGRAM_CHOICES))
        