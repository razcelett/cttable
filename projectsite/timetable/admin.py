from django.contrib import admin
from django.contrib.admin import display
from .models import Student, Faculty, Room, Subject, Schedule, Building, Day

# Register your models here.
# admin.site.register(Buildings)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("email", "student_id", "full_name", "year", "block", "type")
    search_fields = ("email", "student_id", "first_name", "last_name",  "full_name", "year", "block", "type")

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("email","full_name", "department")
    search_fields = ("email", "first_name", "last_name",  "full_name", "department")

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("building_name", "building_location")
    search_fields = ("building_name", "building_location")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_name","room_type")
    search_fields = ("room_name", "room_type")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("class_code","subject_title")
    search_fields = ("class_code","subject_title")

admin.site.register(Day)

admin.site.register(Schedule)
# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ("day","time")
#     search_fields = ("day","time")





# @admin.register(Play)
# class PlayAdmin(admin.ModelAdmin):
#     list_display = ("player","team","string_no","isActive",)

# @admin.register(Match)
# class MatchAdmin(admin.ModelAdmin):
#     list_display = ("team1","score_t1","team2","score_t2","winner",)


