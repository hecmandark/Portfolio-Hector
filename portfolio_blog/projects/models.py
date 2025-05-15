from django.db import models
from datetime import date



class Project(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="projects/images")
    url= models.URLField(blank=True)
    date=models.DateField(default=date.today)
    
    def __str__(self) -> str:
        return self.title
    
    
