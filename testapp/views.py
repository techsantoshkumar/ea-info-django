from django.shortcuts import render,redirect
from testapp.forms import UserForms

# Create your views here. controller


def helloWorld(request):
    form=UserForms()

    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            pass

    d1={
        "form":form
    }
    return render(request,'hello.html',d1)


def testing(request):
    # d1 = {
    #     "name": "",
    #     "email": "m@gmail.com",
    #     "l1": [1, 2, 3, 4, 5],
    #     "d2": {'address': 'BTM', 'city': 'Banglore'}
    # }
    # return render(request, 'test2.html', d1)
    return render(request, 'test2.html')