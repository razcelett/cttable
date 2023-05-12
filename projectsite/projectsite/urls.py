"""projectsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from django.conf import settings #add this
# from django.conf.urls.static import static #add this

from timetable.views import HomePageView, create_student, StudentList, FacultyList,  AdminFacultyList, StudentScheduleList,  FirstBlockOneScheduleList, \
      FirstBlockTwoScheduleList, FirstBlockThreeScheduleList, FirstBlockOneScheduleList, SecondBlockOneScheduleList, SecondBlockTwoScheduleList, SecondBlockThreeScheduleList, \
      ThirdBlockOneScheduleList, FourthBlockOneScheduleList
from timetable import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^student-login/$', auth_views.LoginView.as_view(template_name='student-login.html'), name='student-login'),
    re_path(r'^faculty-login/$', auth_views.LoginView.as_view(template_name='faculty-login.html'), name='faculty-login'),
    # re_path(r'^student-index/$', auth_views.LoginView.as_view(template_name='student-index.html'), name='student-index'),
    # re_path(r'^gebuilding/$', auth_views.LoginView.as_view(template_name='geroom.html'), name='gebuilding'),
    # re_path(r'^nitbuilding/$', auth_views.LoginView.as_view(template_name='nitroom.html'), name='nitbuilding'),
    # re_path(r'^itbuilding/$', auth_views.LoginView.as_view(template_name='itroom.html'), name='itbuilding'),
    re_path(r'^admin-index/$', auth_views.LoginView.as_view(template_name='admin-index.html'), name='index'),
    # re_path(r'^admin-student/$', auth_views.LoginView.as_view(template_name='admin-student.html'), name='students'),
    re_path(r'^admin-faculty/$', auth_views.LoginView.as_view(template_name='admin-faculty.html'), name='faculties'),
    path('itbuilding', views.itrooms, name="itbuilding"),
    path('nitbuilding', views.nitrooms, name="nitbuilding"),
    path('gebuilding', views.gerooms, name="gebuilding"),
    path('student/register', views.create_student, name="student-register"),
    path('faculty/register', views.create_faculty, name="faculty-register"),
    path('student-update', views.student_profileupdate, name="student-update"),
    path('faculty-update', views.faculty_profileupdate, name="faculty-update"),
    path('change_password', views.change_password, name="change_password"),
    path('login', views.student_login, name="student-login"),
    path('logout', views.student_logout, name="student-logout"),
    path('timetable', views.timetable, name="timetable"),
    path('',views.HomePageView.as_view(), name='home'),
    path('students', StudentList.as_view(), name='StudentList'),
    # path('faculties', FacultyList.as_view(), name='FacultyList'),
    path('faculties', views. FacultyList, name='FacultyList'),
    path('faculty', AdminFacultyList.as_view(), name='AdminFacultyList'),
    path('student/schedule/', views.StudentScheduleList, name='StudentScheduleList'),
    path('faculty/schedule/', views.FacultyScheduleList, name='FacultyScheduleList'),
    path('schedules/first-year/block1', FirstBlockOneScheduleList.as_view(), name='FirstBlockOneScheduleList'),
    path('schedules/first-year/block2', FirstBlockTwoScheduleList.as_view(), name='FirstBlockTwoScheduleList'),
    path('schedules/first-year/block3', FirstBlockThreeScheduleList.as_view(), name='FirstBlockThreeScheduleList'),
    path('schedules/second-year/block1', SecondBlockOneScheduleList.as_view(), name='SecondBlockOneScheduleList'),
    path('schedules/second-year/block2', SecondBlockTwoScheduleList.as_view(), name='SecondBlockTwoScheduleList'),
    path('schedules/second-year/block3', SecondBlockThreeScheduleList.as_view(), name='SecondBlockThreeScheduleList'),
    path('schedules/third-year/block1', ThirdBlockOneScheduleList.as_view(), name='ThirdBlockOneScheduleList'),
    path('schedules/fourth-year/block1', FourthBlockOneScheduleList.as_view(), name='FourthBlockOneScheduleList'),
    path('student/schedule/<str:id>/', views.StudentTimeTableView, name='studentschedule'),
    path('faculty/schedule/<str:id>/', views.FacultyTimeTableView, name='facultyschedule'),
    # path('faculty/schedule/edit/<str:id>/', FacultySched.as_view(), name='facultyscheduleedit'),
    path('faculty/schedule/edit/<str:id>/', views.FacultyEditTimeTable, name='facultyscheduleedit'),
    path('subject/add', views.add_subject, name="add-subject"),
    path('schedule/add', views.add_schedule, name="add-schedule"),
    path('schedule/update/<str:id>', views.edit_schedule, name="edit-schedule"),
    path('schedule/delete/<str:id>', views.delete_schedule, name="delete-schedule"),
    path('timetable/download', views.timetable_pdf, name="timetable_pdf"),
    path('student/timetable/download', views.StudentScheduleList_pdf, name="StudentScheduleList_pdf"),
    path('faculty/timetable/download', views.FacultyScheduleList_pdf, name="FacultyScheduleList_pdf"),
]
