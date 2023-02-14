from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Work(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    description = models.CharField(max_length=400,default="")
    slug = models.SlugField(max_length=100, null = True, blank = True)
    time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
