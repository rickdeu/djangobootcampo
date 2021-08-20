from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100, verbose_name="Nome categoria")
    def __str__(self):
        return self.nome_categoria
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome_categoria']