from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .permission import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer,TodoViewSerializer
from datetime import datetime, timezone






class TodoListApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated, IsOwner]

    #1. List all 
    def get(self,request,*args, **kwargs):
        '''
            List all the todo itemms 
        '''
        todos =Todo.objects.filter(user=request.user.id).order_by('-updated')
       
        
        serializer = TodoViewSerializer(todos, many=True)
        res ={

        }
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #2. Create
    def post(self,request,*args, **kwargs):
        '''
            Create a todo item  
        '''
        # data = {
        #     'task': request.data.get('task'),
        #     'priority': request.data.get('priority'),
        #     'is_completed': request.data.get('is_completed'),
        #     'timestamp': request.data.get('timestamp'),
        # }
        data = request.data
        data['user'] = request.user.id

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #u can return a created succussfully message
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, *args, **kwargs):
        '''
            zdelete a todo with a given todo_id 
        '''
        # todo_instance = self.get_object(todo_id, request.user.id)
        todo_instance = Todo.objects.all()
        
        # if not todo_instance:
        #     return Response(
        #         {"msg": "Todo with this id does not exist"},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        todo_instance.delete()
        return Response({"msg": "Todo deleted successfully"}, status=status.HTTP_200_OK)




    
class TodoDetailApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self,todo_id, user_id):
        '''
            Helper method to get the object with the given todo_id 
        '''
        try:
            return Todo.objects.get(id=todo_id, user=user_id)
        except Todo.DoesNotExist:
            return None

    #3  Retrieve a Todo
    def get(self,request, todo_id, *args, **kwargs):
        '''
            Retreves a todo with a given todo_id 
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"msg": "Todo with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TodoViewSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #4  Update a Todo
    def put(self,request, todo_id, *args, **kwargs):
        '''
            Update a todo with a given todo_id  if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"message": "This todo doesn\'t exist"},
                status=status.HTTP_404_NOT_FOUND
                )
        # data = request.data
        
        timer = datetime.now(timezone.utc)
        # todo_instance.is_completed = not todo_instance.is_completed
        data = {
            'task': request.data.get('task'),
            'priority': request.data.get('priority') or todo_instance.priority,
            'updated': timer,
            'is_completed': request.data.get('is_completed') or not todo_instance.is_completed,
        }
        try:
            serializer = TodoViewSerializer(instance=todo_instance,data=data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # if data is not None:
        #     serializer = TodoSerializer(instance=todo_instance,data=data, partial=True)
        #     serializer.is_valid()
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     msg ={
        #         'message':'invalid data'
        #     }
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #6  Delete a Todo
    def delete(self,request, todo_id, *args, **kwargs):
        '''
            delete a todo with a given todo_id 
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        
        if not todo_instance:
            return Response(
                {"msg": "Todo with this id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response({"msg": "Todo deleted successfully"}, status=status.HTTP_200_OK)


