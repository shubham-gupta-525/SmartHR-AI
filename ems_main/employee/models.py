from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(unique = True, max_length = 300)
    salary = models.DecimalField(max_digits = 10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"