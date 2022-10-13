from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Rooms ,Topic, Message
from .serializers import RoomSerializer ,MessageSerializer,UserSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
def getRoutes(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    
    return Response(routes)


@api_view(["GET"])
def getRooms(request):
    rooms = Rooms.objects.all()
    serializar = RoomSerializer(rooms,many=True).data
    return Response(serializar)




@api_view(["GET"])
def getRoom(request,pk):
    room = Rooms.objects.get(id = pk)
    serializar = RoomSerializer(room,many=False).data
    return Response(serializar)



@api_view(["GET"])
def Get_Messages(request):
    mess = Message.objects.all()
    serializar = MessageSerializer(mess,many=True).data
    return Response(serializar)


@api_view(["GET"])
def GET_USERS(request,pk):
    if pk == "true":
        user = User.objects.all()
        serializar = UserSerializer(user,many=True).data
        return Response(serializar)
    else:
        return Response("You Do not have Permission")