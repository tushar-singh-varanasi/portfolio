from django.db import models

# Create your models here.
class About(models.Model):
    about=models.TextField()
    resume=models.FileField(upload_to ='resume/')

    

    def __str__(self):
        return self.about

class Project(models.Model):
    Name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    project_url=models.URLField(max_length=400)
    image=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.Name


class contact(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.Name

    def __unicode__(self):
        return 

