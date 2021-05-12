from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140, null=False)
    date = models.DateTimeField(auto_now_add=True)
    
class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
 
class Followers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    followed-user = models.ForeignKey(User, on_delete=models.CASCADE)
       

"""
    
    #Calcular following 
    
    following = []
    
    for i in range(len(Followers)):
        
        if Followers[i].user == A:
            following.append(Followers[i])
        
        
    
    User: A
    Followed-user: B
    
    Con esto ya sabemos que el usuario A sigue al usuario B
    
    
    #Calcular followers 
    
    followers_array = []
    
    for i in range(len(Followers)):
        
        if Followers[i].Followed-user == A:
            followers_array.append(Followers[i])
    
 

    """
