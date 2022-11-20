
from django import forms

PROGRAM_CHOICES = [
    ('math_comp', 'Joint Mathematics & Computer Science'),
    ('math_comp_hon', 'Joint Honours Mathematics & Computer Science'),
    ('math', 'Mathematics')
]
SEMESTER = [
    ('fall', 'Fall'),
    ('winter', 'Winter')
]
class UserForm(forms.Form):
    program = forms.CharField(label="What program are you in?", required=True, widget=forms.Select(choices=PROGRAM_CHOICES))
    semester = forms.CharField(label="Select starting semester", required=True, widget=forms.RadioSelect(choices=SEMESTER)) 
    courses = forms.CharField(label="Enter courses already taken", required=False) 
