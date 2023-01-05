from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes, renderer_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from tasks.models import Task
from tasks.serializers import TaskSerializer, CreateTaskSerializer

# Create your views here.

# tasks list
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
@permission_classes([IsAuthenticated])
def get_tasks_list(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # print(request.data)
        user=request.user
        data = request.data
        data.update({'user': user.id})
        create_task_serilizer = CreateTaskSerializer(data=data)
        if create_task_serilizer.is_valid():
            # print(create_task_serilizer.data)
            create_task_serilizer.save()
            return Response(create_task_serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'data is wrong :<'}, status=status.HTTP_400_BAD_REQUEST)


# task by id
@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def get_or_update_task_by_id(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response({'message': 'task does not exist :<'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        # get data
        data = request.data
        # update data
        task_serializer = TaskSerializer(task, data=data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'data is wrong :<'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':  
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# task by priority
@api_view(['GET'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def get_tasks_by_priority(request):
    if request.method == 'GET':
        task_priorities = Task.get_priorities()
        return Response(task_priorities, status=status.HTTP_200_OK)

# complete all tasks
@api_view(['PUT'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def complete_all_task(request): 
    if request.method == 'PUT':
        tasks = Task.objects.filter(user=request.user).filter(is_completed=False) 
        for task in tasks: 
            task.is_completed = True
            task.save() 
        return Response(status=status.HTTP_200_OK)

# uncomplete all tasks
@api_view(['PUT'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def uncomplete_all_task(request): 
    if request.method == 'PUT':
        tasks = Task.objects.filter(user=request.user).filter(is_completed=True) 
        for task in tasks: 
            task.is_completed = False
            task.save() 
        return Response(status=status.HTTP_200_OK)

# delete all tasks
@api_view(['DELETE'])
@parser_classes([JSONParser, FormParser])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def delete_all_tasks(request): 
    if request.method == 'DELETE':  
        tasks = Task.objects.filter(user=request.user) 
        for task in tasks: 
            task.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)