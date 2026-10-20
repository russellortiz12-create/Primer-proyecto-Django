from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen")
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"
        return f"{self.title} {public}"


class Category(models.Model):
    name = models.CharField(max_length=110, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="Descripción")
    created_at = models.DateField(verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name