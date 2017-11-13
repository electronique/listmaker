from django.shortcuts import render, HttpResponse, redirect

from models import User
from models import Appointment
# Create your views here.
def index(request):
    return render(request, "pbelt/index.html")

def reg(request):
    request.session['username']= request.POST['username']
    User.objects.create(name=request.POST['name'],username=request.POST['username'],password=request.POST['password'])
    return redirect("/pbelt/appointments")

def appointments(request):
    try:
        request.session['username']=request.POST['username']
    except KeyError:
        request.session['username']   
    user = User.objects.filter(username=request.session['username'])
    print user
    context = {
               "appointments":Appointment.objects.filter(friend=user),
               "reg_user":User.objects.filter(username=request.session['username'])
            }
    return render(request,"pbelt/appointments.html",context)
def logout(request):
    request.session.clear()
    return redirect('/pbelt/')

def add(request,id):
    request.session['username']
    return render(request,'pbelt/add.html',{"users":User.objects.get(id=id)})

def addapt(request):
    request.session['username']
    user = User.objects.filter(username=request.session['username'])
    for u in user:
        schedule = Appointment.objects.filter(friend=u.id)
        print u.id
        if u.username == request.session['username']:
            Appointment.objects.create(friend =User.objects.get(id=u.id), appointment =request.POST['appointment'],date =request.POST['date'],time=request.POST['time'])
    return redirect("/pbelt/appointments")

def show(request,id):
    
    user=User.objects.get(id=id),
    appointments=Appointment.objects.filter(friend=user)
    context = {
        'user':user,
        'appointments':appointments
    }
   
    return render(request, "pythonbelt/show.html",context)

def delete(request,id):
    request.session['username']
    a = Appointment.objects.get(id=id)
    a.delete()  
    return redirect("/pbelt/appointments")

def edit(request,id):
    return render(request, "pbelt/edit.html",{"Appointments":Appointment.objects.get(id=id)})

def editprocess(request,id):
    entry = Appointment.objects.get(id=id)
    entry.appointment = request.POST['appointment']
    entry.date =  request.POST['date']
    entry.time = request.POST['time']
    entry.save()
    
    return redirect("/pbelt/appointments")