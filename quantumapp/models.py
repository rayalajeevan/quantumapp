from django.db import models

# Create your models here.


class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    highest_education = models.CharField(max_length=100)
    company_name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)
    current_skills = models.CharField(max_length=500)
    aspiring_skills = models.CharField(max_length=500)
    aspiring_role = models.CharField(max_length=150)
    dream_company = models.CharField(max_length=150)
    careers_trajectories = models.CharField(
        max_length=10, choices=(("YES", "YES"), ("NO", "NO")))
    create_an_account = models.CharField(
        max_length=10, choices=(("YES", "YES"), ("NO", "NO")))
    password = models.CharField(max_length=150, blank=True, null=True)
