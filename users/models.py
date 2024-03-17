from django.db import models
from django import forms

# Create your models here.


## ===>USER_MODEL 
class CustomUser(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, null=True)
    password = forms.CharField(widget=forms.PasswordInput)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(null= True)    
    

    PERSON_CHOICES =(
        ('ADMIN', 'Admin'),
        ('PATIENT', 'Patient'),
        ('NURSE', 'Nurse'),
    )
    person = models.CharField(max_length=7, choices=PERSON_CHOICES)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)



    def __str__(self):
        return self.email


## ===>PATEIENT_MODEL
class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.TextField(max_length=20, null=True, blank=False)
    city = models.CharField(max_length=50, null = True, blank=True)
    street = models.TextField(max_length=100, null=True, blank=False)
    national_image = models.ImageField() 

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


## ===>NURSE_MODEL
class Nurse(models.Model):
    name = models.CharField(max_length=50)

    DEGREE_CHOICES = (
        ('A', 'Associate Degree in Nursing'),
        ('D', 'Diploma in Nursing'),
        ('L', 'Licensed Practical Nurse'),
        ('AD', 'Advanced practice registered nurses'),
    )
    degree = models.CharField(max_length=7, choices=DEGREE_CHOICES)

    SEPCIALTY_CHOICES = (
        ('1', 'قسم تمريض الباطني والجراحي'),
        ('2', 'قسم تمريض العناية الحرجة والطوارئ'),
        ('3', 'قسم تمريض النسا والتوليد'),
        ('4', 'قسم تمريض الأطفال'),
        ('5', 'قسم التمريض النفسي والصحة العقلية'),
        ('6', 'قسم إدارة التمريض'),
        ('7', 'قسم تمريض المسنين'),
        ('8', 'قسم تمريض صحة المجتمع')
    )
    

    specialty = models.CharField(max_length=50, null=True, blank=True, choices=SEPCIALTY_CHOICES )

    RATING_CHOICES = (
        ('1', 'fine'),
        ('2', 'good'),
        ('3', 'verygood'),
        ('4', 'excilent'),
        ('5', 'Top'),

    )

    avg_rate = models.CharField(max_length=10, choices=RATING_CHOICES)


    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)



    def __str__(self):
        return self.name


## ===>VISIT_MODEL
class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    comments = models.CharField(max_length=2000)




class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)



class service(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.service_name