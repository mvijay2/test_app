from django.db import models
from datetime import date



# Create your models here.
from django.contrib.auth.models import User
from .managers import CustomUserManager


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
#from django.utils.translation import ugettext_lazy as _



class CustomUser(AbstractUser, PermissionsMixin):
    #username=None
    email=models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    def __str__(self):
        return self.email
    
    


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100,blank=True, null=True)
    organization = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=20, choices=[('Meeting', 'Meeting'), ('Training', 'Training'),('Exposure Visit', 'Exposure Visit'), ('Workshop', 'Workshop'),('Demonstration', 'Demonstration'), ('External Visit', 'External Visit'), ('Other', 'Other')],blank=True, null=True)
    from_date = models.DateField(default=date.today)
    to_date = models.DateField(default=date.today)
    location = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    resource_persons = models.CharField(max_length=100,blank=True, null=True)
    male_participants = models.IntegerField(default=0)
    female_participants = models.IntegerField(default=0)
    total_participants = models.IntegerField(default=0)
    photo=models.ImageField(null=True, blank=True, upload_to='images/' )
    document=models.FileField(null=True, blank=True, upload_to='documents/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Add user field



class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=20, choices=[('Photos', 'Photos'), ('Videos', 'Videos'),('Media Coverage', 'Media Coverage')],blank=True, null=True)
    date = models.DateField(default=date.today)

    location = models.CharField(max_length=100,blank=True, null=True)

    document=models.ImageField(null=True, blank=True, upload_to='images/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Add user field activity_name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True)
    email_id = models.EmailField(max_length=50,blank=True, null=True)
    work_location = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    photo=models.ImageField(null=True, blank=True, upload_to='images/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # 

class Resources(models.Model):
    resource_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, choices=[('IEC Material', 'IEC Material'), ('Training Modules', 'Training Modules'),('Training Material', 'Training Material'),('Reports', 'Reports')],blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=100,blank=True, null=True)
    document=models.FileField(null=True, blank=True, upload_to='documents/' )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # 


class Farmersdata(models.Model):
    id = models.CharField(max_length=41, primary_key=True)
    date_widget = models.DateTimeField(blank=True, null=True)
    district = models.CharField(max_length=9,blank=True, null=True)
    ngo = models.CharField(max_length=4,blank=True, null=True)
    surveyer_name = models.CharField(max_length=17,blank=True, null=True)
    designation = models.CharField(max_length=16,blank=True, null=True)
    sub_district = models.CharField(max_length=10,blank=True, null=True)
    revenue_village = models.CharField(max_length=10,blank=True, null=True)
    gp = models.CharField(max_length=12,blank=True, null=True)  # Gram Panchayat
    village = models.CharField(max_length=12,blank=True, null=True)
    farmer_name = models.CharField(max_length=28,blank=True, null=True)
    father_husband_name = models.CharField(max_length=25,blank=True, null=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=2,blank=True, null=True)
    sub_classification = models.CharField(max_length=8,blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    primary_occupation = models.CharField(max_length=13,blank=True, null=True)
    primary_occupation_other = models.CharField(max_length=28, blank=True, null=True)
    job_card_number = models.IntegerField(blank=True, null=True)
    income_sources = models.CharField(max_length=64,blank=True, null=True)
    income_sources_other = models.CharField(max_length=27, blank=True, null=True)
    land_owned = models.CharField(max_length=3,blank=True, null=True)
    total_land_owned = models.DecimalField(max_digits=19, decimal_places=17,blank=True, null=True)
    land_leased_in = models.CharField(max_length=3,blank=True, null=True)
    land_leased_out = models.CharField(max_length=3,blank=True, null=True)
    livestock_owned = models.CharField(max_length=3,blank=True, null=True)
    irrigation_sources = models.CharField(max_length=3,blank=True, null=True)
    type_irrigation_sources = models.CharField(max_length=25,blank=True, null=True)
    type_irrigation_sources_other = models.CharField(max_length=12, blank=True, null=True)
    job_card_owned = models.CharField(max_length=3,blank=True, null=True)
    is_women_headed_family = models.CharField(max_length=3,blank=True, null=True)
    is_single_women_family = models.CharField(max_length=3,blank=True, null=True)
    migration_from_family = models.CharField(max_length=3,blank=True, null=True)
    member_in_institution = models.CharField(max_length=3,blank=True, null=True)
    in_which_institution = models.CharField(max_length=75,blank=True, null=True)
    in_which_institution_other = models.CharField(max_length=31, blank=True, null=True)
    hh_has_kitchen_garden = models.CharField(max_length=3,blank=True, null=True)
    hh_head_family_photo = models.CharField(max_length=17, blank=True, null=True)

    
    class Meta:
        ordering = [
            "id", "date_widget", "district", "ngo", "surveyer_name", "designation",
            "sub_district", "revenue_village", "gp", "village", "farmer_name",
            "father_husband_name", "gender", "age", "category", "sub_classification",
            "phone_number", "primary_occupation", "primary_occupation_other",
            "job_card_number", "income_sources", "income_sources_other", "land_owned",
            "total_land_owned", "land_leased_in", "land_leased_out", "livestock_owned",
            "irrigation_sources", "type_irrigation_sources", "type_irrigation_sources_other",
            "job_card_owned", "is_women_headed_family", "is_single_women_family",
            "migration_from_family", "member_in_institution", "in_which_institution",
            "in_which_institution_other", "hh_has_kitchen_garden", "hh_head_family_photo"
        ]

    def __str__(self):
        return f"{self.farmer_name} ({self.village})"

    