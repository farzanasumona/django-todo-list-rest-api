from datetime import datetime

from rest_framework import serializers

from TodoListApp.models import Task


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    is_done = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    desc = serializers.CharField()

    def create(self, data):
        return Task.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.is_done = data.get('is_done', instance.is_done)
        instance.desc = data.get('desc', instance.desc)
        instance.update_at = datetime.now()

        instance.save()
        return instance