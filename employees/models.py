from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)  # New field
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])  # New field
    date_of_birth = models.DateField(null=True, blank=True)  # Allow null values
    email = models.EmailField(unique=True)  # New field
    mobile_number = models.CharField(max_length=15, unique=True)  # New field
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
