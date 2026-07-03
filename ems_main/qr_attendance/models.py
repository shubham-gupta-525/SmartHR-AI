from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos/')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        # Save first so emp_id exists
        super().save(*args, **kwargs)

        # Generate QR with emp_id only
        qr_data = self.emp_id

        qr = qrcode.make(qr_data)
        qr_io = BytesIO()
        qr.save(qr_io, format='PNG')

        file_name = f"{self.emp_id}_qr.png"
        self.qr_code.save(file_name, File(qr_io), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Attendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    total_time = models.DurationField(null=True, blank=True)

    def calculate_total_time(self):
        if self.time_in and self.time_out:
            time_in_dt = datetime.combine(self.date, self.time_in)
            time_out_dt = datetime.combine(self.date, self.time_out)

            if time_out_dt > time_in_dt:
                self.total_time = time_out_dt - time_in_dt

    def save(self, *args, **kwargs):
        self.calculate_total_time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
