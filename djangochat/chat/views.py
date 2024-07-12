from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    return render(request,'room.html',{'username':username,'room':room,'room_details':room_details})


def checkview(request):
    if(request.method=='POST'):
        roomname=request.POST.get('room_name')
        username=request.POST.get('username')

    if Room.objects.filter(name=roomname).exists():
        return redirect('/'+roomname+'/?username='+username)
    else:
        new_room=Room.objects.create(name=roomname)
        new_room.save()
        return redirect('/'+roomname+'/?username='+username)

    pass

def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


