from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
class Year(models.Model):
    year_choice = models.CharField(max_length=15, blank=True, null=True, default=None)
    
    def __str__(self):
        return self.year_choice
    
    class Meta:
        verbose_name_plural = 'Years'

class Block(models.Model):
    block_choice = models.CharField(max_length=15, blank=True, null=True, default=None)

    def __str__(self):
        return self.block_choice
    
    class Meta:
        verbose_name_plural = 'Blocks'

class Type(models.Model):
    type_choice = models.CharField(max_length=15, blank=True, null=True, default=None)

    def __str__(self):
        return self.type_choice
    
    class Meta:
        verbose_name_plural = 'Student Type'

class Student(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    student_id = models.CharField(max_length=20, unique=True, help_text="Format: ####-##-#####")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name = "Year", null=True, blank=True, default=None)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name = "Block", null=True, blank=True, default=None)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name = "Type", null=True, blank=True, default=None)
    student_profile_picture = models.ImageField(null=True, blank=True, upload_to="static/img/student_prof_pic/")

    def __str__(self):
        if self.middle_name:
            # DELACRUZ, Juan P.
            return f'{self.last_name.upper()}, {self.first_name.upper()} {"".join(m[0].upper() for m in self.middle_name.split(" "))}.'        
        # DELACRUZ, Juan
        return f'{self.last_name.upper()}, {self.first_name.upper()}'
    
    def full_name(self):
        if self.middle_name:
            return f'{self.last_name.upper()}, {self.first_name.upper()} {"".join(m[0].upper() for m in self.middle_name.split(" "))}.' 
        return f'{self.last_name.upper()}, {self.first_name.upper()}'

    class Meta:
        verbose_name_plural = 'Students'

class Faculty(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    department_choice=[('Computer Studies Department', 'Computer Studies Department')]
    department = models.CharField(max_length=50, choices=department_choice, default=None)
    faculty_profile_picture = models.ImageField(null=True, blank=True, default=None, upload_to="static/img/faculty_prof_pic/")

    def __str__(self):
        if self.middle_name:
            # DELACRUZ, Juan P.
            return f'{self.last_name.upper()}, {self.first_name.upper()} {"".join(m[0].upper() for m in self.middle_name.split(" "))}.'        
        # DELACRUZ, Juan
        return f'{self.last_name.upper()}, {self.first_name.upper()}'
    
    def full_name(self):
        if self.middle_name:
            return f'{self.last_name.upper()}, {self.first_name.upper()} {"".join(m[0].upper() for m in self.middle_name.split(" "))}.' 
        return f'{self.last_name.upper()}, {self.first_name.upper()}'

    class Meta:
        verbose_name_plural = 'Faculties'

class Building(models.Model):
    building_name = models.CharField(max_length=30)
    building_location = models.CharField(max_length=30, default=None, null=True, blank=True)
    building_picture = models.ImageField(null=True, blank=True, upload_to="static/img/building_picture/")


    def __str__(self):
        return f'{self.building_name}'
    
    class Meta:
        verbose_name_plural = 'Buildings'

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name = "Building", null=True, blank=True, default=None)
    room_name = models.CharField(max_length=30)
    room_type = models.CharField(max_length=30, null=True, blank=True)
    room_picture = models.ImageField(null=True, blank=True, upload_to="static/img/room_picture/")


    def __str__(self):
        return f'{self.room_name}, {self.room_type}'
    
    class Meta:
        verbose_name_plural = 'Rooms'

class Subject(models.Model):
    class_code = models.CharField(max_length=30)
    subject_title = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.subject_title}'

    class Meta:
        verbose_name_plural = 'Subjects'

class Schedule(models.Model):
    week_day=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))
    day = models.CharField(max_length=10, choices=week_day, default=None, null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name = "subjects")
    students = models.ManyToManyField(Student, related_name = "students")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name = "Faculty", null=True, blank=True)
    year_section = models.ForeignKey(Year, on_delete=models.CASCADE, related_name = "year_section", null=True, blank=True)
    block_section = models.ForeignKey(Block, on_delete=models.CASCADE, related_name = "block_section", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name = "Room", null=True, blank=True)

    def __str__(self):
        return f'{self.day}'
    
    class Meta:
        verbose_name_plural = 'Schedules'


