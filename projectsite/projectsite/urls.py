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

from timetable.views import HomePageView, create_student, StudentList, FacultyList, StudentScheduleList
from timetable import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^student-login/$', auth_views.LoginView.as_view(template_name='student-login.html'), name='student-login'),
    re_path(r'^faculty-login/$', auth_views.LoginView.as_view(template_name='faculty-login.html'), name='faculty-login'),
    # re_path(r'^student-index/$', auth_views.LoginView.as_view(template_name='student-index.html'), name='student-index'),
    # re_path(r'^gebuilding/$', auth_views.LoginView.as_view(template_name='geb.html'), name='gebuilding'),
    # re_path(r'^nitbuilding/$', auth_views.LoginView.as_view(template_name='nitb.html'), name='nitbuilding'),
    # re_path(r'^itbuilding/$', auth_views.LoginView.as_view(template_name='itb.html'), name='itbuilding'),
    path('itbuilding', views.itrooms, name="itbuilding"),
    path('nitbuilding', views.nitrooms, name="nitbuilding"),
    path('gebuilding', views.gerooms, name="gebuilding"),
    path('student-register', views.create_student, name="student-register"),
    path('student-update', views.student_profileupdate, name="student-update"),
    path('student_login', views.student_login, name="student-login"),
    path('student_logout', views.student_logout, name="student-logout"),
    path('',views.HomePageView.as_view(), name='home'),
    path('student_list', StudentList.as_view(), name='StudentList'),
    path('faculty_list', FacultyList.as_view(), name='FacultyList'),
    path('student_schedule', StudentScheduleList.as_view(), name='StudentScheduleList'),
    

]