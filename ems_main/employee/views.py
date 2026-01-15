from django.shortcuts import render,redirect, get_object_or_404
from .models import Employee
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']
        phone = int(request.POST['phone'])
        email = request.POST['email']
        salary = float(request.POST['salary'])
        hire_date = request.POST['hire_date']

        n_emp = Employee(
            first_name = first_name,
            last_name = last_name,
            role = role,
            phone = phone,
            email = email,
            salary = salary,
            hire_date = hire_date
        )
        n_emp.save()
        messages.success(request, "Employee added successfully!")
        return redirect('add_emp')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
def remove_emp(request):
    emps=Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

def delete_emp(request, emp_id):
    emp = get_object_or_404(Employee, id = emp_id)
    emp.delete()
    messages.success(request, "Employee removed successfully!")
    return redirect('remove_emp')


def filter_emp(request):
    emps = Employee.objects.all()

    name = request.GET.get('name')
    role = request.GET.get('role')
    email = request.GET.get('email')

    if name:
        emps = emps.filter(
            Q(first_name__icontains=name) |
            Q(last_name__icontains=name)
        )
    if role:
        emps = emps.filter(role__icontains=role)
    if email:
        emps = emps.filter(email__icontains=email)

    context = {
        'emps': emps
    }

    return render(request, 'filter_emp.html', context)

def home(request):
    return render(request, 'home.html')

