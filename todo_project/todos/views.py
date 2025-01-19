from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User, Todo
from .serializers import UserSerializer, TodoSerializer
from .permissions import IsAuthorOrAdmin
from django.shortcuts import render

def frontend_view(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.pk)

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):

        data = request.data
        data['password'] = make_password(data.get('password'))
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def login(request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=400)


    def reset_password(request):
        user = request.user
        new_password = request.data.get('new_password')
        user.password = make_password(new_password)
        user.save()
        return Response({"message": "Password reset successful"})

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_todos(self, request):

        todos = Todo.objects.filter(author=request.user)
        serializer = self.get_serializer(todos, many=True)
        return Response(serializer.data)

