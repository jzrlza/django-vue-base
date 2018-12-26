from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

import json
import bcrypt

from .models import *

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



class PostsView(ListAPIView):
    authentication_class = (JSONWebTokenAuthentication,) # Don't forget to add a 'comma' after first element to make it a tuple
    #permission_classes = (IsAuthenticated,)



#@ensure_csrf_cookie
@csrf_exempt
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            user = None
            return HttpResponse(user)

        if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) :
            print("It Matches!")
        else:
            user = None

        return HttpResponse(user)
    else:
        return None


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            user = None

        if user :
            return HttpResponse('User already Exists')
        else :
            encrypt_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            new_user = User(username=data['username'],password=encrypt_password.decode('utf-8'))
            new_user.save()

            return HttpResponse('Success')
    else:
        return None
