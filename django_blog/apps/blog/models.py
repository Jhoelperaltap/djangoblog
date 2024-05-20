from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la categoria', max_length=100, null = False, blank= True)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.nombre
    

class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField('Nombres del autor', max_length=255, null = False, blank= True)
    apellidos = models.CharField('Apellidos del autor', max_length=255, null = False, blank= True)
    facebook = models.URLField('Facebook', null =True, blank = True)
    twitter = models.URLField('Twitter', null =True, blank = True)
    instagram = models.URLField('Instagram', null =True, blank = True)
    web = models.URLField('Web', null =True, blank = True)
    email = models.EmailField('Email del autor', max_length=255, null = False, blank= True)
    estado = models.BooleanField('Autor Activo/ No Activo', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)
    
class Post(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=90, blank= False, null = False)
    slug = models.CharField('Slug', max_length= 100, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length= 110, blank = False, null = False)
    contenido = CKEditor5Field('Contenido', config_name='default')
    imagen = models.URLField(max_length= 255, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add= True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.titulo
    
    
