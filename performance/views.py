from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Avg
from .models import Marks, Subject, Student
from django.core.cache import cache

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'performance/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if request.user.is_authenticated:
                cache_key = f'student_dashboard_{request.user.id}'
                cache.delete(cache_key)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'performance/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_dashboard(request):
    user_id = request.user.id
    cache_key = f'student_dashboard_{user_id}'
    context = cache.get(cache_key)

    if not context:
        student = request.user
        marks = Marks.objects.filter(student=student).select_related('subject')

        # Highest scorer in each subject
        highest_scorers = Marks.objects.values('subject__name').annotate(max_marks=Max('marks_obtained'))

        # Overall highest scorer
        overall_highest_scorer = Marks.objects.values('student__username').annotate(avg_marks=Avg('marks_obtained')).order_by('-avg_marks').first()

        context = {
            'marks': marks,
            'highest_scorers': highest_scorers,
            'overall_highest_scorer': overall_highest_scorer
        }

        cache.set(cache_key, context, 60 * 15)  # Cache for 15 minutes

    return render(request, 'performance/dashboard.html', context)

def redirect_to_login(request):
    return redirect('login')


