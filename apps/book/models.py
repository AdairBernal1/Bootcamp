from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    publication_date = models.DateField(verbose_name='Fecha de Publicacion')
    pages = models.PositiveSmallIntegerField(verbose_name='Numero de Paginas')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Categoria')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return '%s (%s)' % (self.title, self.publication_date)
