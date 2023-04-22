from django.contrib import admin
from django.contrib.admin import display
from .models import Student, Faculty, Room, Subject, Schedule, Building, Year, Block, Type

# Register your models here.
# admin.site.register(Buildings)
admin.site.register(Year)
admin.site.register(Block)
admin.site.register(Type)

# @admin.register(Time)
# class TimeAdmin(admin.ModelAdmin):
#     list_display = ("start_time", "end_time")
#     search_fields = ("start_time", "end_time")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("email", "student_id", "full_name", "year", "block")
    search_fields = ("email", "student_id", "first_name", "last_name",  "full_name", "year", "block")

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
    
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("day","year_section", "block_section", "subjects", "faculty", "start_time","end_time")
    list_display = ("day","year_section", "block_section", "subjects", "faculty", "start_time","end_time")
# admin.site.register(Day)

# admin.site.register(Schedule)





