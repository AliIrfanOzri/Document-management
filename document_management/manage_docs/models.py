from django.db import models

# Create your models here.
from django.db import models

class Folders(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name

class Digital_Documents(models.Model):
    i_folders = models.ForeignKey(Folders, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name

class Topics(models.Model):
    i_documents = models.ForeignKey(Digital_Documents, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name

