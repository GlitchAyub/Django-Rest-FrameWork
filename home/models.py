import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class BaseModel(models.Model):
    user = models.ForeignKey(User,on_delete =  models.SET_NULL,null = True,blank=True)
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    

class TimingTodo(BaseModel):
    todo =models.ForeignKey(Todo,on_delete=models.CASCADE)
    timing = models.DateField()
