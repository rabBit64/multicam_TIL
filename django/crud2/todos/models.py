from django.db import models

class Todo(models.Model):
  title = models.CharField(max_length=80)
  content	= models.TextField(	null=True)
  completed = models.BooleanField(	default=False)
  priority = models.IntegerField(default=3)
  created_at = models.DateField(auto_now_add=True)
  deadline = models.DateField(null=True)


