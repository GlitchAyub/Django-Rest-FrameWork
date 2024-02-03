from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Todo

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
            "message": "Invalid data",
        })
