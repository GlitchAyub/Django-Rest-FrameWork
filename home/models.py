import uuid
from django.db import models
from django.utils.translation import gettext as _

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    title = models.CharField( max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
