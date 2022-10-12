from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RoomForm
from .models import Rooms, Topic, Message
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from django.contrib import messages
rooms = [
    {'id': 1, 'name': 'lets Learn Python'},
    {'id': 2, 'name': 'Design me'},
    {'id': 3, 'name': 'Fontend Developer'},

]


def Login_form(request):
    page = "login"
    if request.method == 'POST':
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        try:
            user = User.objects.get(username=username)
        except:
            ''
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.add_message(request, messages.INFO, 'Error while Login...')
    context = {'page': page}
    return render(request, 'Login.html', context)


def settings(request):
    return render (request,'Setting.html' )

def registerUser(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                user.username = user.username.lower()
            except:
                ""
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.add_message(request, messages.INFO, 'Error while Registering...')
    return render(request, 'Login.html', {"form": form})


@login_required(login_url="login")
def DeleteMassage(request, pk):
    messag = Message.objects.get(id=pk)
    if request.user != messag.user:
        return HttpResponse("You are not Allowed, only Owner Can delete.")
    if request.method == "POST" :
        messag.delete()
        return redirect(to="home")
    return render(request, 'delete.html', {"obj": messag})


def index(request):
    q = None
    try:
        q = request.GET["q"]
    except:
        q = ''
    topics = Topic.objects.all()

    rooms = Rooms.objects.filter(topic__name__icontains=q)
    room_count = rooms.count()
    recent_massages = Message.objects.filter(room__topic__name__icontains=q).order_by("-created")
    # .order_by("-created")
    return render(request, "index.html", {'rooms': rooms, "topics": topics, 'room_count': room_count, "recent_massages": recent_massages})


def UserProfile(request, pk):
    userr = User.objects.get(id=pk)
    rooms = userr.rooms_set.all()
    room_count = rooms.count()
    recent_massages = userr.message_set.all().order_by("-created")
    topics = Topic.objects.all()
    context = {'room_count':room_count,'user': userr,'rooms':rooms,"recent_massages":recent_massages,"topics":topics}
    return render(request, 'profile.html', context)


def room(request, pk):
    pk = int(pk)
    room = Rooms.objects.get(id=pk)
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    roommessages = room.message_set.all().order_by("-created")
    return render(request, 'room.html', {"room": room, "roommessages": roommessages, "participants": participants})


@login_required(login_url="login")
def CreateRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    context = {'form': form,"topics":topics}
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            print("YEs")
            gg = form.save(commit=False)
            gg.host = request.user
            gg.save()
            return redirect("home")
    else:
        print("NO")
    return render(request, "form.html", context)


@login_required(login_url="login")
def Updateform(request, pk):
    room = Rooms.objects.get(id=pk)
    form = RoomForm(instance=room)
    print(request.user)
    if request.user != room.host:
        return HttpResponse("You are not Allowed, only Owner Can Modify.")
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'form.html', context)


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Rooms.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not Allowed, only Owner Can delete.")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, 'delete.html')


def LogoutUser(request):
    logout(request)
    return redirect('home')
