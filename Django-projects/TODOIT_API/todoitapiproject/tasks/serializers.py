from rest_framework import serializers
from tasks.models import Task
from accounts.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Task
        fields = [
            'id', 
            'title', 
            'short_description', 
            'description', 
            'priority', 
            'is_completed',
            'user'
        ]
        # fields = '__all__'
        # exclude = ['user']

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description', 
            'short_description', 
            'priority', 
            'user'
        ]