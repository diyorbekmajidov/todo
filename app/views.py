from django.shortcuts import render
from .serializers import TodoSerializer, UserSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.
class CreateUserView(APIView):
    def post(self, request):
        """
        url: https://majidovdiyorbek.pythonanywhere.com/api/create/
        Create a new user
        input: json->{
            "username": "username", 
            "password": "password",
            "email": "email",
            "first_name": "first_name",
            "last_name": "last_name"

        }
        """
        if request.method == 'POST':
        # Get the user data from the request data
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            token= Token.objects.create(user=user)
            # Return the user data and token
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        
        return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogOut(APIView):
    """
    Logout a user
    input: https://majidovdiyorbek.pythonanywhere.com/api/logout/
    
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class UserLogIn(APIView):
    """
    url: https://majidovdiyorbek.pythonanywhere.com/api/userlogin/
    Login a user
    input: json->{
        "username": "username",
        "password": "password"
        }
        """
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        if token:
            token.delete()
        token= Token.objects.create(user=user)
        return Response({"token":token.key})

class GetAllUsers(APIView):
    """
    Get all users
    input: https://majidovdiyorbek.pythonanywhere.com/api/getusers/

    """
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(instance=data, many=True)
        return Response(serializer.data)

class CreateTodo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new todo
        input: json->{
            "title": "title",
            "important": "important"
        }
            """
        data = request.data
        data['user'] = request.user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self, request):
        """
        Get all todos
        input: https://majidovdiyorbek.pythonanywhere.com/api/create/
        return: json->{
            "title": "title",
            "important": "important",
        }
        """
        user = request.user
        data = Todo.objects.filter(user=user)
        serializer = TodoSerializer(instance=data, many=True)
        return Response(serializer.data)
    
class TodoGetId(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        """
        Get todo by id
        input: https://majidovdiyorbek.pythonanywhere.com/api/gettodo/id/
        return: json->{
            "title": "title",
            "important": "important",
        }
        
        """
        user = request.user
        data = Todo.objects.filter(user=user, id=pk)
        serializer = TodoSerializer(instance=data, many=True)
        return Response(serializer.data)
    
class TodoUpdate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        """
        Update todo by id
        input: https://majidovdiyorbek.pythonanywhere.com/api/updatetodo/id/
        return: json->{
            "title": "title",
            "important": "important",
        }
        
        """
        user = request.user
        data = Todo.objects.get(user=user, id=pk)
        serializer = TodoSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TodoDelete(APIView):
    def post(self, request, pk):
        """
        Delete todo by id
        input: https://majidovdiyorbek.pythonanywhere.com/api/deletetodo/id/
        return: j{"OK delete":"200"}
        """
        user = request.user
        data = Todo.objects.get(user=user, id=pk)
        data.delete()
        return Response({"status":200})

        

