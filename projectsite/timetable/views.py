from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .forms import LoginForm, StudentForm, UpdateStudentForm, FacultyForm, ChangePasswordForm
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

# student list of faculties from the database view
@method_decorator(login_required, name='dispatch')
class AdminFacultyList(ListView):
    model = Faculty
    context_object_name = 'faculty'
    template_name = 'admin-faculty-view.html'
    paginated_by = 10

    #getting the data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    #filter (search function)
    def get_queryset(self, *args, **kwargs):
        qs = super(AdminFacultyList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("last_name")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("last_name").filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(email__icontains=query) | Q(department__icontains=query))
        return qs

@method_decorator(login_required, name='dispatch')
class FacultyList(ListView):
    model = Faculty
    context_object_name = 'faculty'
    template_name = 'student-faculty-view.html'
    paginated_by = 10

    #getting the data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    #filter (search function)
    def get_queryset(self, *args, **kwargs):
        qs = super(FacultyList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("last_name")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("last_name").filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(email__icontains=query) | Q(department__icontains=query))
        return qs

# faculty list of students from the database view
@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'admin-student.html'
    # paginated_by = 10

    #getting the data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    #filter (search function)
    def get_queryset(self, *args, **kwargs):
        qs = super(StudentList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("last_name")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("last_name").filter(Q(first_name__icontains=query)| Q(last_name__icontains=query) | Q(email__icontains=query))
        return qs

# student timetable view
@method_decorator(login_required, name='dispatch')
class StudentScheduleList(ListView):
    model = Schedule
    context_object_name = 'Student_Schedule'
    template_name = 'student-index.html'
    User = Student
    # paginated_by = 10

    #getting the data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
# ----------------------------------------------------------------

#student update profile'
@login_required()
def student_profileupdate(request):
    msg = None
    success = False
    student = Student.objects.filter(email=request.user.email).first()
    print(f'request.user.is_authenticated: {request.user.is_authenticated}')


    if request.user.is_authenticated:
        current_user = Student.objects.get(id=student.id)
        form = UpdateStudentForm(request.POST or None, instance=current_user)

        if request.method == 'POST':
            form = UpdateStudentForm(request.POST or None, instance=current_user)
            print(f'files: {request.FILES}')
            if form.is_valid():
                print('saving items123...')
                print(f'errors: {form.errors}')
                for key, value in form.cleaned_data.items():
                    print(f'key: {key} value: {value}')

                form.save()
                if request.FILES.get('student_profile_picture') is not None:
                    student.student_profile_picture = request.FILES.get('student_profile_picture')
                    student.save()
                    print('profile picture saved successfully')
                
                msg = 'Your Profile has been updated'
                return redirect("StudentScheduleList")
            return render(request, 'student-profile.html', {'form': form})
        elif request.method == 'GET':
            print(f'student profile: {student.student_profile_picture}')

            return render(request, 'student-profile.html', {'form': form, 'student_profile': student.student_profile_picture})
        
    else:
        msg = 'Failed to update your Profile'


def change_password(request):
    context = { 'segment': 'change-password' }
    context['form'] = ChangePasswordForm(user=request.user)

    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            print(f'form is valid: {form}')
            form.save()
            return redirect("/")
        else:
            print(f'form is invalid: {form}')
            context['form'] = form
            return render(request, 'change-password.html', context)

    return render(request, 'change-password.html', context)

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

def create_faculty(request):
    msg = None
    success = False
    form = FacultyForm()

    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'User created successfully.'
            success = True
            return redirect("AdminFacultyList")
    
    else:
        msg = 'Form is not valid'
        success = False

    return render(request, 'faculty-register.html', {'form': form, 'msg': msg, 'success': success})

# it building view rooms
def itrooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'itb.html', context)

# nit building view rooms
def nitrooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'nitb.html', context)

# ge building view rooms
def gerooms(request):
    room = Room.objects.all().order_by('room_name')
    context = {'room':room}
    return render(request, 'geb.html', context)




