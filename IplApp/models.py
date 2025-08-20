from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Franchise(models.Model):
    name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    coach_name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    founded_year=models.IntegerField()
    logo=models.ImageField(blank=True, null=True, upload_to='franchises_logos')

    class Meta:
        db_table='franchise'


    def __str__(self):
        return f"{self.name} ({self.short_name})"


class Player(models.Model):
    ROLE_CHOICES = [
        ('Batsman','Batsman'),
        ('Bowler','Bowler'),
       ( 'All-Rounder','All-Rounder'),
       ( 'Wicket-Keeper','Wicket-Keeper')
    ]
    name=models.CharField(max_length=100)
    age=models.PositiveBigIntegerField()
    role=models.CharField(max_length=50,choices=ROLE_CHOICES)
    nationality=models.CharField(max_length=50)
    franchise=models.ForeignKey(Franchise,on_delete=models.CASCADE)
    photo=models.ImageField(null=True,blank=True,upload_to='player_photos') 

    def __str__(self):
        return f"{self.name} ({self.role})"
    
class Stadium(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    capacity=models.PositiveIntegerField()
    established_year=models.PositiveIntegerField()   
    home_team=models.ForeignKey(Franchise,on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.name} ({self.city})"
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    profile_photo = models.ImageField(upload_to='profile_photos',blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"
   