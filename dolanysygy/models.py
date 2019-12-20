from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Welayatlar(models.Model):
    ady     = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural =("Welayatlar")
    def __str__(self):
        return self.ady

class Edaralar(models.Model):
    ady     = models.CharField(max_length=200)
    welayaty= models.ForeignKey(Welayatlar,models.CASCADE)
    class Meta:
        verbose_name_plural =("Edaralar")
    def __str__(self):
        return self.ady

class Bolumler(models.Model):
    ady     = models.CharField(max_length=200)
    edarasy = models.ForeignKey(Edaralar,models.CASCADE)
    welayaty= models.ForeignKey(Welayatlar,models.CASCADE)
    class Meta:
        verbose_name_plural =("Bolumler")
    def __str__(self):
        return self.ady

class Hasabat(models.Model):
    ady     = models.CharField(max_length=200)
    bolumi  = models.ForeignKey(Bolumler,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural =("Hasabat")
    def __str__(self):
        return self.ady

class Ulanyjy(AbstractUser):
    ady         = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural =("Ulanyjylar")
    def __str__(self):
        return self.ady        

class File(models.Model):
    ady      = models.CharField(max_length=200)
    ulanyjy  = models.ForeignKey(Ulanyjy,on_delete=models.CASCADE)
    dokement = models.FileField(upload_to='Dokumentler')
    döredilen_senesi  = models.DateTimeField(auto_now=True)
    üýgedilen_senesi  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural =("Faýl")
    def __str__(self):
        return self.ady

