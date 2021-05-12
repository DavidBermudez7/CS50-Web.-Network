from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    
    following = strings = JSONField(default=list, blank=True, null=True)
    
    """
    - Following: Array
    - Followers: ??? 
        - La interración de followers se realiza por otra persona que da a seguir a este.
          Esto genera que de singuna de las maneras sea posible que el usuario al que están siguiendo sea capaz de añadir este seguidor a su base de datos.
          Por tanto la opción más lógica sería hacer una query a la database y preguntarle cuantos seguidores te usuario tiene. 
          Después podemos pasar esto como parámetro a la vista y usar el argumento count. 
          

    """
    pass


#Post

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140, null=False)
    date = models.DateTimeField(auto_now_add=True)
    
class Likes(models.Model)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField(auto_now_add=True)


"""

    USER:
        - CORREO
        - PASSWORD
        - CONTRASEÑA
        - ID
    
    POST:
        - USUARIO
        - ID
        - TEXTO 
        - FECHA 
        
        
    LIKES: 
        - POST 
        - USUARIO 
        - DATE
        
"""



"""
    #LOS MUESTRA EN LA FOTO PERO NO DICE NADA DE ELLOS EN LAS ESPECIFICACIONES SO??
    COMMENTS:
    
        - POST 
        - USUARIO 
        - DATE 
"""
