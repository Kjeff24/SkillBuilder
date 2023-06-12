from django.db import models

# Create your models here.
# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.id} - {self.name}"