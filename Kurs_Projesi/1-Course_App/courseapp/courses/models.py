from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False,unique=True,db_index=True, max_length=50)

    def __str__(self):
        return f"{self.name}"

# RichTextField()

class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=250,default="")
    description = models.TextField()
    image = models.ImageField(upload_to="images",default="")
    date= models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False, unique=True, db_index=True) 
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")

class Comment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    create_at = models.DateTimeField(auto_now_add=True)




