from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    admission_date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.student_name
