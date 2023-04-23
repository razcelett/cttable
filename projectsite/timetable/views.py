from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .forms import LoginForm, StudentForm, UpdateStudentForm, FacultyForm, ChangePasswordForm, UpdateFacultyForm
from .models import Student, Faculty, Schedule, Room, Subject
from django.db.models import Q
from django.contrib.auth.models import User




#login
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

# loginrequred decorator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    paginated_by = 10

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
# class StudentScheduleList(LoginRequiredMixin, ListView):
#     model = Schedule
#     context_object_name = 'Student_Schedule'
#     template_name = 'student-index.html'
#     # paginated_by = 10

#     def get_queryset(self):
#         # get the logged in user
#         user = self.request.user
        
#         # get the student object associated with the user
#         student = Student.objects.filter(email=user.email).first()
        
#         # filter the schedules based on the student's year and block
#         queryset = Schedule.objects.filter(students__in=[student], year_section=student.year, block_section=student.block)

        
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

# ----------------------------------------------------------------

#student update profile'
from django.contrib import messages

@login_required()
def student_profileupdate(request):
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
                
                messages.success(request, 'Your Profile has been updated')
                return redirect("student-update")
            else:
                messages.error(request, 'Failed to update your Profile')
            return render(request, 'student-profile.html', {'form': form})
        elif request.method == 'GET':
            print(f'student profile: {student.student_profile_picture}')

            return render(request, 'student-profile.html', {'form': form, 'student_profile': student.student_profile_picture})
        
    else:
        messages.error(request, 'Failed to update your Profile')
        return render(request, 'student-profile.html')


@login_required()
def faculty_profileupdate(request):
    success = False
    faculty = Faculty.objects.filter(email=request.user.email).first()
    print(f'request.user.is_authenticated: {request.user.is_authenticated}')


    if request.user.is_authenticated:
        current_user = Faculty.objects.get(id=faculty.id)
        form = UpdateFacultyForm(request.POST or None, instance=current_user)

        if request.method == 'POST':
            form = UpdateFacultyForm(request.POST or None, instance=current_user)
            print(f'files: {request.FILES}')
            if form.is_valid():
                print('saving items123...')
                print(f'errors: {form.errors}')
                for key, value in form.cleaned_data.items():
                    print(f'key: {key} value: {value}')
                

                form.save()
                if request.FILES.get('faculty_profile_picture') is not None:
                    faculty.faculty_profile_picture = request.FILES.get('faculty_profile_picture')
                    faculty.save()
                    print('profile picture saved successfully')
                
                messages.success(request, 'Your Profile has been updated')
                return redirect("faculty-update")
            else:
                   msg = 'Failed to update your Profile'
                   return render(request, 'faculty-profile.html', {'form': form})
        elif request.method == 'GET':
            print(f'faculty profile: {faculty.faculty_profile_picture}')

            return render(request, 'faculty-profile.html', {'form': form, 'faculty_profile': faculty.faculty_profile_picture})
        
    else:
        messages.error(request, 'Failed to update your Profile')


def change_password(request):
    context = { 'segment': 'change-password' }
    context['form'] = ChangePasswordForm(user=request.user)

    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            print(f'form is valid: {form}')
            form.save()
            messages.success(request, 'Change Password Success.')
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
                try:
                    login(request, user)
                    if request.user.is_superuser:
                        return redirect("timetable")
                    elif not request.user.is_superuser and not any(char.isdigit() for char in user.email):
                        # Redirect to FacultyScheduleList
                        return redirect("FacultyScheduleList")
                    else:
                        return redirect("StudentScheduleList")
                except ValidationError:
                    msg = 'Invalid credentials'
            
            msg = 'Invalid credentials'

    # else:
    #     # msg = 'Login failed'

    return render(request, 'student-login.html', {'form': form, 'msg':msg})

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
            messages.success(request, 'User Created Successfully')
            success = True
            return redirect("StudentList")
    
        else:
            # messages.error(request, 'Form is not valid')
            success = False

    return render(request, 'student-register.html', {'form': form, 'success': success})

def create_faculty(request):
    msg = None
    success = False
    form = FacultyForm()

    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully')
            success = True
            return redirect("AdminFacultyList")
    
        else:
            messages.error(request, 'Form is not valid')
            success = False

    return render(request, 'faculty-register.html', {'form': form, 'success': success})

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

def timetable(request):
    schedules = Schedule.objects.all().order_by("day", "start_time")

    grouped_schedules = {}
    for schedule in schedules:
        key = (schedule.day,)
        if key in grouped_schedules:
            grouped_schedules[key].append(schedule)
        else:
            grouped_schedules[key] = [schedule]

    merged_schedules = []
    for key in grouped_schedules:
        schedules = grouped_schedules[key]
        if len(schedules) > 1:
            day = schedules[0].day
            merged_schedule = {
                'start_time': [s.start_time for s in schedules],
                'end_time': [s.end_time for s in schedules],
                'faculty': [s.faculty for s in schedules],
                'subjects': [s.subjects for s in schedules],
                'rooms': [s.subjects.room for s in schedules],
                'day': day
            }
            merged_schedules.append(merged_schedule)
        else:
            schedule = schedules[0]
            merged_schedules.append({
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'faculty': schedule.faculty,
                'subjects': schedule.subjects,
                'rooms': schedule.subjects.room,
                'day': schedule.day
            })

    context = {'schedules': merged_schedules}
    return render(request, 'student-index.html', context)


@login_required(login_url='login')
def StudentTimeTableView(request, id):
    try:
        student = Student.objects.get(id=id)
        courses = Subject.objects.all()
        professors = Faculty.objects.all()
        rooms = Room.objects.all()

        # Get schedules for the student's block and year, or all schedules if the student's block and year is not set
        if student.block and student.year:
            schedules = Schedule.objects.filter(year_section=student.year, block_section=student.block).order_by("day", "start_time")

            grouped_schedules = {}
            for schedule in schedules:
                key = (schedule.day,)
                if key in grouped_schedules:
                    grouped_schedules[key].append(schedule)
                else:
                    grouped_schedules[key] = [schedule]

            merged_schedules = []
            for key in grouped_schedules:
                schedules = grouped_schedules[key]
                if len(schedules) > 1:
                    day = schedules[0].day
                    merged_schedule = {
                        'start_time': [s.start_time for s in schedules],
                        'end_time': [s.end_time for s in schedules],
                        'faculty': [s.faculty for s in schedules],
                        'subjects': [s.subjects for s in schedules],
                        'rooms': [s.subjects.room for s in schedules],
                        'day': day
                    }
                    merged_schedules.append(merged_schedule)
                else:
                    schedule = schedules[0]
                    merged_schedules.append({
                        'start_time': schedule.start_time,
                        'end_time': schedule.end_time,
                        'faculty': schedule.faculty,
                        'subjects': schedule.subjects,
                        'rooms': schedule.subjects.room,
                        'day': schedule.day
                    })

        # else:
        #     schedules = Schedule.objects.all()

        context = {'student': student, 'courses': courses, 'professors': professors, 'rooms': rooms, 'schedules': merged_schedules}
        return render(request, 'student-timetable.html', context)
    
    except Student.DoesNotExist:
        messages.error(request, 'Student does not exist')
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'admin-student.html', context)
    
@login_required(login_url='login')
def FacultyTimeTableView(request, id):
    try:
        faculty = Faculty.objects.get(id=id)
        courses = Subject.objects.all()
        rooms = Room.objects.all()

        # Get schedules for the student's block and year, or all schedules if the student's block and year is not set
        if faculty.id :
            schedules = Schedule.objects.filter(faculty=faculty.id).order_by("day", "start_time")

            grouped_schedules = {}
            for schedule in schedules:
                key = (schedule.day,)
                if key in grouped_schedules:
                    grouped_schedules[key].append(schedule)
                else:
                    grouped_schedules[key] = [schedule]

            merged_schedules = []
            for key in grouped_schedules:
                schedules = grouped_schedules[key]
                if len(schedules) > 1:
                    day = schedules[0].day
                    merged_schedule = {
                        'start_time': [s.start_time for s in schedules],
                        'end_time': [s.end_time for s in schedules],
                        'faculty': [s.faculty for s in schedules],
                        'subjects': [s.subjects for s in schedules],
                        'rooms': [s.subjects.room for s in schedules],
                        'year': [s.year_section.year_choice for s in schedules],
                        'block': [s.block_section.block_choice for s in schedules],
                        'day': day
                    }
                    merged_schedules.append(merged_schedule)
                else:
                    schedule = schedules[0]
                    merged_schedules.append({
                        'start_time': schedule.start_time,
                        'end_time': schedule.end_time,
                        'faculty': schedule.faculty,
                        'subjects': schedule.subjects,
                        'rooms': schedule.subjects.room,
                        'year': schedule.year_section.year_choice,
                        'block': schedule.block_section.block_choice,
                        'day': schedule.day
                    })

        # else:
        #     schedules = Schedule.objects.all()

        context = {'faculty': faculty, 'courses': courses, 'rooms': rooms, 'schedules': merged_schedules}
        return render(request, 'faculty-timetable.html', context)
    
    except Faculty.DoesNotExist:
        messages.error(request, 'Faculty does not exist')
        faculty = Faculty.objects.all()
        context = {'faculty': faculty}
        return render(request, 'admin-faculty-view.html', context)
    
    
@login_required(login_url='login')
def StudentScheduleList(request):
    try:
        # Get the logged in user's student object
        student = Student.objects.filter(email=request.user.email).first()

        courses = Subject.objects.all()
        professors = Faculty.objects.all()
        rooms = Room.objects.all()

        # Get schedules for the student's block and year, or all schedules if the student's block and year is not set
        if student.block and student.year:
            schedules = Schedule.objects.filter(year_section=student.year, block_section=student.block).order_by("day", "start_time")

            grouped_schedules = {}
            for schedule in schedules:
                key = (schedule.day,)
                if key in grouped_schedules:
                    grouped_schedules[key].append(schedule)
                else:
                    grouped_schedules[key] = [schedule]

            merged_schedules = []
            for key in grouped_schedules:
                schedules = grouped_schedules[key]
                if len(schedules) > 1:
                    day = schedules[0].day
                    merged_schedule = {
                        'start_time': [s.start_time for s in schedules],
                        'end_time': [s.end_time for s in schedules],
                        'faculty': [s.faculty for s in schedules],
                        'subjects': [s.subjects for s in schedules],
                        'rooms': [s.subjects.room for s in schedules],
                        'day': day
                    }
                    merged_schedules.append(merged_schedule)
                else:
                    schedule = schedules[0]
                    merged_schedules.append({
                        'start_time': schedule.start_time,
                        'end_time': schedule.end_time,
                        'faculty': schedule.faculty,
                        'subjects': schedule.subjects,
                        'rooms': schedule.subjects.room,
                        'day': schedule.day
                    })

        context = {'student': student, 'courses': courses, 'professors': professors, 'rooms': rooms, 'schedules': merged_schedules}
        return render(request, 'student-index.html', context)
    
    except Student.DoesNotExist:
        messages.error(request, 'Student does not exist')
        students = Student.objects.all()
        context = {'students': students}
        return render(request, 'student-index.html', context)
    
    
@login_required(login_url='login')
def FacultyScheduleList(request):
    try:
        faculty = Faculty.objects.filter(email=request.user.email).first()
        courses = Subject.objects.all()
        rooms = Room.objects.all()

        # Get schedules for the student's block and year, or all schedules if the student's block and year is not set
        if faculty.id :
            schedules = Schedule.objects.filter(faculty=faculty.id).order_by("day", "start_time")

            grouped_schedules = {}
            for schedule in schedules:
                key = (schedule.day,)
                if key in grouped_schedules:
                    grouped_schedules[key].append(schedule)
                else:
                    grouped_schedules[key] = [schedule]

            merged_schedules = []
            for key in grouped_schedules:
                schedules = grouped_schedules[key]
                if len(schedules) > 1:
                    day = schedules[0].day
                    merged_schedule = {
                        'start_time': [s.start_time for s in schedules],
                        'end_time': [s.end_time for s in schedules],
                        'faculty': [s.faculty for s in schedules],
                        'subjects': [s.subjects for s in schedules],
                        'rooms': [s.subjects.room for s in schedules],
                        'year': [s.year_section.year_choice for s in schedules],
                        'block': [s.block_section.block_choice for s in schedules],
                        'day': day
                    }
                    merged_schedules.append(merged_schedule)
                else:
                    schedule = schedules[0]
                    merged_schedules.append({
                        'start_time': schedule.start_time,
                        'end_time': schedule.end_time,
                        'faculty': schedule.faculty,
                        'subjects': schedule.subjects,
                        'rooms': schedule.subjects.room,
                        'year': schedule.year_section.year_choice,
                        'block': schedule.block_section.block_choice,
                        'day': schedule.day
                    })

        # else:
        #     schedules = Schedule.objects.all()

        context = {'faculty': faculty, 'courses': courses, 'rooms': rooms, 'schedules': merged_schedules}
        return render(request, 'student-index.html', context)
    
    except Faculty.DoesNotExist:
        messages.error(request, 'Faculty does not exist')
        faculty = Faculty.objects.all()
        context = {'faculty': faculty}
        return render(request, 'student-index.html', context)
    

    


    






