from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_class', 'admission_date']

    def clean_student_name(self):
        name = self.cleaned_data.get('student_name')
        if not name:
            raise forms.ValidationError("This field is required.")
        return name
