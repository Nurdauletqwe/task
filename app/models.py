from django.db import models

class Rubric(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Айди')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'Name: {self.name}'
    
    class Meta:
        verbose_name = 'Рубрика',
        verbose_name_plural = 'Рубрики'