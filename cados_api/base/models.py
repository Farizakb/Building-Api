from django.db import models

# Create your models here.


class Advocat(models.Model):
    username = models.CharField(max_length=150)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username