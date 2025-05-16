from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def student_list(request):
    query = request.GET.get('q')
    students = Student.objects.filter(is_deleted=False)
    if query:
        students = students.filter(Q(student_name__icontains=query) | Q(student_class__icontains=query))
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.soft_delete()
    return redirect('student_list')
