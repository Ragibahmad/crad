from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length = 150, default="other")
    def __str__(self):
        return self.name
    

class Component(models.Model):
    title = models.CharField(max_length = 150)
    desc = models.TextField(help_text="describe the component code")
    image = models.FileField(upload_to="images", default="card.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    
    