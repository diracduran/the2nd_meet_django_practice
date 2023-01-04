from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 
            'title', 
            'short_description', 
            'description', 
            'priority', 
            'is_completed'
        ]
        # fields = '__all__'
        # exclude = ['user']

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 
            'description', 
            'priority', 
        ]