
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path('todo/', TodoView.as_view(), name='todo-view'),
    path('', include(router.urls)),
    path('post-todo/',post_todo,name='post_todo'),
    path('get-todo/',get_todo,name='get_todo'),
]


