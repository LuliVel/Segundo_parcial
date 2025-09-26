from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    curso_inscrito = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
