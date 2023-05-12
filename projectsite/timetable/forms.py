from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import re
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import TimePickerInput


from .models import Student, Faculty, Year, Block, Type, Subject, Schedule, Room

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your current password'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a new password'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your new password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    
    
class StudentForm(ModelForm):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    })
    )
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password",
            "id": "password"
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password",
            "id": "confirm_password"
        })
    )
    student_id = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Student ID (####-##-####)"
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name"
        })
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Middle name (Optional)",
        }),
        required=False
    )
    # year_choices = [('1st', 'First Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4th', 'Fourth Year')]
    # year = forms.ChoiceField(
    #     year_choices=Student.year_choice,
    #     widget=forms.Select(attrs={
    #         "class": "form-control",
    #         "placeholder": "Select your Year Level"
    #     })
    # )
    # block_choices = [('1', 'Block 1'), ('2', 'Block 2'), ('3', 'Block 3'), ('4', 'Block 4')]
    # block = forms.ChoiceField(
    #     block_choices=Student.block_choice,
    #     widget=forms.Select(attrs={
    #         "class": "form-control",
    #         "placeholder": "Select your Year Block"
    #     })
    # )

    year = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Year"
        }),
        queryset = Year.objects.all(), initial = 0,
    )
    block = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Block"
        }),
        queryset = Block.objects.all(), initial = 0,
    )
    type = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Status"
        }),
        queryset = Type.objects.all(), initial = 0,
    )



    class Meta:
        model = Student
        fields = ['student_profile_picture','email', 'username','password', 'confirm_password', 'student_id', 'first_name', 'last_name', 'middle_name', 'year', 'block', 'type']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if not re.match(r'^\d{4}-\w{1,5}-\w{2,5}$', student_id):
            raise forms.ValidationError("Invalid student ID format")
        return student_id

    def save(self, commit=True):
        student = super().save(commit=False)
        # user = get_user_model().objects.create_user(email=self.cleaned_data['email'], password=self.cleaned_data['password'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
        user = get_user_model().objects.create_user(email=self.cleaned_data['email'], username=self.cleaned_data['username'], password=self.cleaned_data['password'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
        user.username = user.username
        # user.username = user.email
        user.save()
        student.account = user
        if commit:
            student.save()
        return student

class UpdateStudentForm(ModelForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name"
        })
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Middle name (Optional)",
        }),
        required=False
    )
    year = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Year"
        }),
        queryset = Year.objects.all(), initial = 0,
    )
    block = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Block"
        }),
        queryset = Block.objects.all(), initial = 0,
    )
    type = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Status"
        }),
        queryset = Type.objects.all(), initial = 0,
    )
    student_profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control",
            "placeholder": "Upload your profile picture"
        })
    )

    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'year', 'block', 'type']

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if not re.match(r'^\d{4}-\w{1,5}-\w{2,5}$', student_id):
            raise forms.ValidationError("Invalid student ID format")
        return student_id
    
    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student

class FacultyForm(ModelForm):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    })
    )
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password",
            "id": "password"
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm password",
            "id": "confirm_password"
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name"
        })
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Middle name (Optional)",
        }),
        required=False
    )
    department = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Department"
        }),
        choices=Faculty.department_choice,
    )

    class Meta:
        model = Faculty
        fields = ['faculty_profile_picture', 'email', 'username','password', 'confirm_password', 'first_name', 'last_name', 'middle_name', 'department']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password


    def save(self, commit=True):
        faculty = super().save(commit=False)
        # user = get_user_model().objects.create_user(email=self.cleaned_data['email'], password=self.cleaned_data['password'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
        user = get_user_model().objects.create_user(email=self.cleaned_data['email'], username=self.cleaned_data['username'], password=self.cleaned_data['password'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
        user.username = user.username
        # user.username = user.email
        user.save()
        faculty.account = user
        if commit:
            faculty.save()
        return faculty
    
class UpdateFacultyForm(ModelForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name"
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name"
        })
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Middle name (Optional)",
        }),
        required=False
    )
    department = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Select your Department"
        }),
        choices=Faculty.department_choice,
    )
    faculty_profile_picture = forms.ImageField(
        required=False, widget=forms.ClearableFileInput(attrs=
            {"class": "form-control",
            "placeholder": "Upload your profile picture"})
    )


    class Meta:
        model = Faculty
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'department', 'faculty_profile_picture']
    
    def save(self, commit=True):
        faculty = super().save(commit=False)
        if commit:
            faculty.save()
        return faculty

class SubjectForm(ModelForm):
    class_code = forms.CharField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Class Code"
    })
    )
    subject_title = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject Title"
        })
    )

    class Meta:
        model = Subject
        fields = ['class_code', 'subject_title']


    def save(self, commit=True):
        subject = super().save(commit=False)
        if commit:
            subject.save()
        return subject
    
class ScheduleForm(ModelForm):
    day = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Day"
        }),
        choices=Schedule.week_day,
    )
    start_time = forms.TimeField(
        widget=TimePickerInput(attrs={
            "class": "form-control",
            "placeholder": "Start Time (24hr format)"
        }
        )
    )
    end_time = forms.TimeField(
        widget=TimePickerInput(attrs={
            "class": "form-control",
            "placeholder": "End Time (24hr format)"
        }
        )
    )
    subjects = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Subjects"
        }),
        queryset=Subject.objects.all(),
    )
    faculty = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Faculty"
        }),
        queryset=Faculty.objects.all(),
        to_field_name='first_name',
    )
    room = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Room"
        }),
        queryset=Room.objects.all(),
    )
    year_section = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Year"
        }),
        queryset=Year.objects.all(),
        to_field_name='year_choice',
    )
    block_section = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Block"
        }),
        queryset=Block.objects.all(),
        to_field_name='block_choice',
    )

    class Meta:
        model = Schedule
        fields = ['day', 'start_time', 'end_time', 'subjects', 'faculty', 'room', 'year_section', 'block_section']


    def save(self, commit=True):
        schedule = super().save(commit=False)
        if commit:
            schedule.save()
        return schedule
    
class UpdateScheduleForm(ModelForm):
    day = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Day"
        }),
        choices=Schedule.week_day,
    )
    start_time = forms.TimeField(
        widget=TimePickerInput(attrs={
            "class": "form-control",
            "placeholder": "Start Time (24hr format)"
        }
        )
    )
    end_time = forms.TimeField(
        widget=TimePickerInput(attrs={
            "class": "form-control",
            "placeholder": "End Time (24hr format)"
        }
        )
    )
    subjects = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Subjects"
        }),
        queryset=Subject.objects.all(),
    )
    faculty = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Faculty"
        }),
        queryset=Faculty.objects.all(),
       
    )
    room = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Room"
        }),
        queryset=Room.objects.all(),
    )
    year_section = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Year"
        }),
        queryset=Year.objects.all(),
       
    )
    block_section = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Block"
        }),
        queryset=Block.objects.all(),
       
    )

    class Meta:
        model = Schedule
        fields = ['day', 'start_time', 'end_time', 'subjects', 'faculty', 'room', 'year_section', 'block_section']


    def save(self, commit=True):
        schedule = super().save(commit=False)
        if commit:
            schedule.save()
        return schedule
    









