from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.http import JsonResponse
from . models import *
from django.db.models import Q
from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query == None:
            query = ''

    # http://127.0.0.1:9090/advocates/?query=Ifiok
    # data = ['Ifiok', 'Yusuf', 'UT']
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

@api_view(['POST'])
def add_advocate(request):
    Advocate.objects.create(
        username = request.data['username']
    )
    return Response('added')

@api_view(['GET', 'PUT', 'DELETE'])
def advocate_details(request, username):
    advocate = Advocate.objects.get(username=username)
    if request.method == 'GET':
        
        serializer = AdvocateSerializer(advocate, many=False)
        data = [username]
        return Response(serializer.data)
    # {"username":"Ifiok", "bio": "I just updated my bio"}
    if request.method =='PUT':
        advocate.username = request.data['username']
        advocate.username = request.data['bio']
        advocate.save()

    if request.method =='DELETE':
        advocate.delete()
        return Response('User was deleted')