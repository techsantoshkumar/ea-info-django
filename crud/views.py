from django.shortcuts import render,redirect
from crud.forms import EmployeeForm
from testapp.models import Employee
from django.db import connection
from django.contrib.auth.decorators import login_required

# Create your views here.


def homePage(request):

    return render(request,'home.html')

def create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            emp = Employee()
            emp.emp_name = form_data['emp_name']
            emp.emp_email = form_data['emp_email']
            emp.emp_address = form_data['emp_address']
            emp.save()
            return redirect(index)

    data ={
        "form": form
    }
    return render(request,'crud/create.html',data)


@login_required(login_url='/signin')
def index(request):
    # select * from employee
    data = Employee.objects.all()
    return render(request,'crud/index.html',{"data":data})
# data key we are passing in index page as a result set the fetch each and every as a dictonary
def update(request):

    id = request.GET['id']
    data = Employee.objects.get(id=id) #reading single line
    form = EmployeeForm(instance=data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form_data = form.cleaned_data
            emp = Employee()
            emp.id = id #update
            emp.emp_name = form_data['emp_name']
            emp.emp_email = form_data['emp_email']
            emp.emp_address = form_data['emp_address']
            emp.save()
            return redirect(index)
    d1={"form":form}
    return render(request,'crud/update.html',d1)


def delete(request):

    id = request.GET['id']
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)


def view(request):
    id = request.GET['id']
    data = Employee.objects.get(id=id)

    return render(request,'crud/view.html',{"data":data})


