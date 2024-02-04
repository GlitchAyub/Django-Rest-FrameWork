from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer,TimingTodoSerializer
from .models import Todo,TimingTodo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            "status":200,
            "message":"django is working",
            "method":"get"
        })
    elif request.method == 'POST':
        return Response({
            "status":200,
            "message":"django is working",
            "method":"POST"
        })
    elif request.method == 'PATCH':
        return Response({
            "status":200,
            "message":"django is working",
            "method":"PATCH"
        })
    else:  
        return Response({
            "status":400,
            "message":"django is working",
            "method":"get"
        })     
       
@api_view(['Get'])
def get_todo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSerializer(todo_obj,many=True)
    return Response({
                "status": True,
                "message": "success",
                'data': serializer.data
            })
    
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            
            return Response({
                "status": True,
                "message": "success",
                'data': serializer.data
            })

        return Response({
            "status": False,
            "message": "invalid-data",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            "status": False,
            "message": "invalid-data",
        })
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        uid = data.get('uid')

        if not uid:
            return Response({
                "status": False,
                "message": "Invalid data",
                "data": {}
            })

        todo_obj = Todo.objects.get(uid=uid)
        serializer = TodoSerializer(todo_obj, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Success",
                'data': serializer.data
            })

        return Response({
            "status": False,
            "message": "Invalid data",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            "status": False,
            "message": "Invalid Uid",
            "error":e
        })        

# class based view

class TodoView(APIView):
    def get(self,request):
        todo_obj = Todo.objects.all()
        serializer = TodoSerializer(todo_obj,many=True)
        return Response({
                "status": True,
                "message": "success",
                'data': serializer.data
            })
        
    def post(self,request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
            
                return Response({
                    "status": True,
                    "message": "success",
                    'data': serializer.data
                })

            return Response({
                "status": False,
                "message": "invalid-data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "message": "invalid-data",
            })
            


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['get'])
    def get_date_to_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs,many=True)
        return Response({
                    "status": True,
                    "message": "success",
                    'data': serializer.data
                })
        
        
    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": True,
                    "message": "success",
                    'data': serializer.data
                })
            return Response({
                "status": False,
                "message": "invalid-data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "message": "invalid-data",
            })
