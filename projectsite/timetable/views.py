from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .forms import LoginForm, StudentForm, UpdateStudentForm
from .models import Student, Faculty, Schedule, Room
from django.db.models import Q
from django.contrib.auth.models import User



#login
from django.contrib.auth import authenticate, login, logout

# loginrequred decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

#Landing page view
class HomePageView(TemplateView):
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class FacultyList(ListView):
    model = Faculty
    context_object_name = 'faculty'
    template_name = 'student-faculty-view.html'
    paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(FacultyList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("last_name")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("last_name").filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(email__icontains=query) | Q(department__icontains=query))
        return qs

@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student-faculty-view.html'
    paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("last_name")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("last_name").filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(email__icontains=query) | Q(year__icontains=query) | Q(block__icontains=query) | Q(type__icontains=query))
        return qs

# @method_decorator(login_required, name='dispatch')
# # class StudentScheduleList(ListView):
# #     model = Schedule
# #     context_object_name = 'schedule'
# #     template_name = 'student-index.html'

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         return context

class StudentScheduleList(ListView):
    model = Schedule
    context_object_name = 'Student_Schedule'
    template_name = 'student-index.html'
    # paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = "__all__"
#     context_object_name = 'student'
#     template_name = 'student-profile.html'
#     success_url = "/student-index"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    
# ----------------------------------------------------------------

@login_required()
def student_profileupdate(request):
    msg = None
    success = False
    student = Student.objects.filter(email=request.user.email).first()
    if request.user.is_authenticated:
        current_user = Student.objects.get(id=student.id)
        form = StudentForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            msg = 'Your Profile has been updated'
            return redirect("/student-index/")
        return render(request, 'student-profile.html', {'form': form})
    else:
        msg = 'Failed to update your Profile'

# def student_profileupdate(request):
#     # student = Student.objects.filter(email=request.user.email).first()
#     student_profile = Student.objects.get(id=request.user.id)
#     form = StudentForm(request.POST or None, instance=student_profile)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect("/student-index/")
    
#     else:
#         msg = 'Failed to update your Profile'

#     return render(request, 'student-profile.html', {'student_profile' : student_profile, 'form' : form})

# def student_profileupdate(request, student_id):
#     student_profile = Student.objects.get(id=student_id)
#     form = StudentForm(request.POST or None, instance=student_profile)
#     if form.is_valid():
#         form.save()
#         return redirect("/student-index/")
#     else:
#         msg = 'Failed to update your Profile'
#     return render(request, 'student-profile.html', {'student_profile' : student_profile, 'form' : form})

#student login
def student_login(request):
    msg = None
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect("StudentScheduleList")
            else:
                msg = 'Invalid credentials'

    # else:
    #     # msg = 'Login failed'

    return render(request, 'student-login.html', {'form': form, 'msg': msg})

#student logout
def student_logout(request):
    logout(request) 
    messages.success = (request, ("Successfully Logged Out"))

#student signup
def create_student(request):
    msg = None
    success = False
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created successfully.'
            success = True
            return redirect("student-login")
    
    else:
        msg = 'Form is not valid'
        success = False

    return render(request, 'student-register.html', {'form': form, 'msg': msg, 'success': success})

def itrooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'itb.html', context)

def nitrooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'nitb.html', context)

def gerooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'geb.html', context)



