from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from TodoListApp.models import Task
from TodoListApp.serializers import TaskSerializer


@api_view(['POST'])
def todo_task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def todo(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        return Response({'error': 'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return Response({'delete': True}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoSearch(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Task.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset

