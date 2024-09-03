from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class newApplication(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Mobile_no=models.CharField(max_length=20)
    
    appoptions=(
        ('caste','Caste'),
        ('income','Income'),
        ('non-creamy','Non creamy'),
        ('possession','Possession'),
        ('etapp','Etapp'),
        ('landtax','Landtax'),
        ('irctc','IRCTC')
    )
    Application_type=models.CharField(max_length=20, choices=appoptions)
    Application_no=models.CharField(max_length=20)
    statusoptions=(
        ('approved','Approved'),
        ('pending','Pending'),
        ('rejected','Rejected'),
        ('none','None')
    )
    Application_status=models.CharField(max_length=10, choices=statusoptions)
    
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Date=models.DateField()
