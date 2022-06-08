from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  create_time = models.DateTimeField(default=timezone.now)
  update_time = models.DateTimeField(default=timezone.now)
  limit_date = models.DateTimeField(null=False)
  status = models.BooleanField(default=False)