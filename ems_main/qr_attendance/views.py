from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            return redirect('id_card', employee.id)
    else:
        form = EmployeeForm()
    return render(request, 'register.html', {'form': form})


def id_card(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'id_card.html', {'employee': employee})


from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Attendance
from datetime import date

def mark_attendance_page(request):
    return render(request, 'mark_attendance.html')

def format_duration(duration):
    if not duration:
        return "--"

    total_seconds = int(duration.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return f"{hours} hrs {minutes} mins"


def process_attendance(request, emp_id):
    try:
        employee = Employee.objects.get(emp_id=emp_id)
    except Employee.DoesNotExist:
        return render(request, 'attendance_failed.html')

    today = date.today()

    attendance, created = Attendance.objects.get_or_create(
        employee=employee,
        date=today
    )

    current_time = timezone.localtime().time()   # ✅ IST time object

    if attendance.time_in is None:
        attendance.time_in = current_time
        attendance.save()

    elif attendance.time_out is None:
        attendance.time_out = current_time
        attendance.save()
    else:
        # Already completed attendance
        pass


    formatted_time = format_duration(attendance.total_time)

    return render(request, 'attendance_success.html', {
        'name': employee.name,
        'total_time': formatted_time
    })


def home(request):
    return render(request, 'home.html')

def attendance_list(request):
    records = Attendance.objects.select_related('employee').all()

    name = request.GET.get('name')
    emp_id = request.GET.get('emp_id')
    email = request.GET.get('email')
    date = request.GET.get('date')

    if name:
        records = records.filter(employee__name__icontains=name)

    if emp_id:
        records = records.filter(employee__emp_id__icontains=emp_id)

    if date:
        records = records.filter(date=date)

    for r in records:
        r.formatted_total = format_duration(r.total_time)

    context = {
        'records': records
    }


    return render(request, 'attendance_list.html', context)


from django.http import HttpResponse
from openpyxl import Workbook
from .models import Attendance

def export_attendance_excel(request):
    records = Attendance.objects.select_related('employee').all()

    #  SAME FILTERS AS PAGE
    name = request.GET.get('name')
    emp_id = request.GET.get('emp_id')
    date = request.GET.get('date')

    if name:
        records = records.filter(employee__name__icontains=name)

    if emp_id:
        records = records.filter(employee__emp_id__icontains=emp_id)

    if date:
        records = records.filter(date=date)

    #  CREATE EXCEL
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance"

    # Header
    ws.append([
        "Employee Name",
        "Employee ID",
        "Email",
        "Date",
        "Time In",
        "Time Out",
    ])

    # Data
    for r in records:
        ws.append([
            r.employee.name,
            r.employee.emp_id,
            r.employee.email,
            r.date.strftime("%d-%m-%Y"),
            r.time_in.strftime("%H:%M:%S") if r.time_in else "",
            r.time_out.strftime("%H:%M:%S") if r.time_out else "",
        ])

    # Response
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="attendance.xlsx"'

    wb.save(response)
    return response

from django.db.models import Q
from .models import Employee

def view_employees(request):
    query = request.GET.get('q')

    if query:
        employees = Employee.objects.filter(
            Q(name__icontains=query) |
            Q(position__icontains=query)
        )
    else:
        employees = Employee.objects.all()

    return render(request, 'view_employees.html', {
        'employees': employees,
        'query': query
    })
