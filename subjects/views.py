from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Subject, Content

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'subjects/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('subjects')
    return render(request, 'subjects/login.html')

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})

@login_required
def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    content = Content.objects.filter(subject=subject)
    return render(request, 'subjects/subject_detail.html', {'subject': subject, 'content': content})
