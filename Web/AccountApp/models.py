from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class User(AbstractUser):
    pass

class Specialty(models.Model):
    name= models.CharField(max_length=100)

phone_validator = RegexValidator(
regex=r"^\d{8}$",
message="Le téléphone doit contenir 8 chiffres."
)

class Doctor(User):
 license_number = models.CharField(
 max_length=6, unique=True,
 validators=[MinLengthValidator(6)]
 )
 phone = models.CharField(
 max_length=8, validators=[phone_validator]
 )
 specialties = models.ManyToManyField('Specialty' , related_name='doctors')


class Patient(User):
 national_id = models.CharField(max_length=8, unique=True)
 phone = models.CharField(max_length=8)
 birth_date = models.DateField()

