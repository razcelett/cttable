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
    # account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    student_id = models.CharField(max_length=20, unique=True, help_text="Format: ####-##-#####")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    # year_choice=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year')]
    # year = models.CharField(max_length=15, choices=year_choice, default=None)
    # block_choice=[('Block 1', 'Block 1'), ('Block 2', 'Block 2'), ('Block 3', 'Block 3'), ('Block 4', 'Block 4')]
    # block = models.CharField(max_length=10, choices=block_choice, default=None)
    # type_choice=[('Regular', 'Regular'), ('Irregular', 'Irregular')]
    # type = models.CharField(max_length=10, choices=type_choice, default=None)
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
    department_choice=[('Computer Studies Department', 'Computer Studies Department'), ('Math Department', 'Math Department')]
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
    room_type = models.CharField(max_length=30)
    room_picture = models.ImageField(null=True, blank=True, upload_to="static/img/room_picture/")


    def __str__(self):
        return f'{self.room_name}, {self.room_type}'
    
    class Meta:
        verbose_name_plural = 'Rooms'

class Subject(models.Model):
    class_code = models.CharField(max_length=30)
    subject_title = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name = "Faculty", null=True, blank=True, default=None)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name = "Room", null=True, blank=True, default=None)
    
    def __str__(self):
        return f'{self.subject_title}'

    class Meta:
        verbose_name_plural = 'Subjects'

class Day(models.Model):
    week_day = models.CharField(max_length=10, default=None)


    def __str__(self):
        return f'{self.week_day}'
    
    class Meta:
        verbose_name_plural = 'Days'

class Time(models.Model):
    start_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f'{self.start_time}, {self.end_time}'
    
    class Meta:
        verbose_name_plural = 'Time'

class Schedule(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name = "day", null=True, blank=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name = "starttime", null=True, blank=True, default=None)
    # end_time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name = "endtime", null=True, blank=True, default=None)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name = "subjects", null=True, blank=True)
    # subjects = models.ManyToManyField(Subject, related_name = "subjects", null=True, blank=True)
    # students = models.ManyToManyField(Student, related_name = "students", null=True, blank=True)
    year_section = models.ForeignKey(Year, on_delete=models.CASCADE, related_name = "year_section", null=True, blank=True, default=None)
    block_section = models.ForeignKey(Block, on_delete=models.CASCADE, related_name = "block_section", null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.day}'
    
    class Meta:
        verbose_name_plural = 'Schedules'


