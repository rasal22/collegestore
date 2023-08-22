from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User,auth

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Create your views here.



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'Invalid username or password ')
            return redirect('login')

    return render(request,"login.html")

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         # if not username:
#         #     messages.info(request, 'enter username')
#         #     return render(request,'login_user')
#
#         # if not password:
#         #     messages.info(request, 'enter password')
#         #     return render(request,'login_user')
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('newpage')
#         else:
#             messages.info(request, 'Invalid username or password')
#
#             return redirect('login')
#
#     else:
#         return render(request, 'login.html')
#

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if len(username)==0:
            messages.info(request, 'Please enter data')
            return render(request,'registration.html')

        if not password:
            return render(request,'registration.html')

        if password !=password1:
            messages.info(request, 'Mismatch Password')
            return render(request,'registration.html')
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.is_staff = False
                user.save()
                return redirect('login')
    else:
        print("this is not post method")
        return render(request, 'registration.html')



def newpage(request):
    return render(request,'newpage.html')


# def form(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone = request.POST['phone']
#
#         if not name:
#             return render(request, 'form.html')
#
#         if not phone:
#             return render(request, 'form.html')
#         user = auth.authenticate(name=name, phone=phone)
#         if user is not None:
#
#             return redirect('form.html')
#         else:
#             # messages.info(request, 'submit accepted')
#             return redirect('confirmation')
#
#     departmentobj = DepartmentModel.objects.all()
#     courseobj = CourseModel.objects.all()
#     return render(request, "form.html", {"Department": departmentobj, "Course": courseobj})
#



def logout(request):
    auth.logout(request)
    return redirect('/')

