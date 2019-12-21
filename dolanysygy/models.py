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
    welaýaty= models.ForeignKey(Welayatlar,models.CASCADE)
    class Meta:
        verbose_name_plural =("Edaralar")
    def __str__(self):
        return self.ady

class Bolumler(models.Model):
    ady     = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural =("Bolumler")
    def __str__(self):
        return self.ady

class Hasabat(models.Model):
    ady     = models.CharField(max_length=200)
    bölümi  = models.ForeignKey(Bolumler,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural =("Hasabat")
    def __str__(self):
        return self.ady

class Ulanyjy(AbstractUser):
    ady         = models.CharField(max_length=200,blank=True)
    welaýaty    = models.ForeignKey(Welayatlar,on_delete=models.CASCADE,null=True)
    edarasy     = models.ForeignKey(Edaralar,on_delete=models.CASCADE,null=True)
    bölümi      = models.ForeignKey(Bolumler,on_delete=models.CASCADE,null=True)
    mac_adresi  = models.CharField(max_length=200,blank=True)
    class Meta:
        verbose_name_plural =("Ulanyjylar")
    def __str__(self):
        return self.username        

class File(models.Model):
    ady                 = models.CharField(max_length=200)
    eýesi               = models.ForeignKey(Ulanyjy,on_delete=models.CASCADE)
    welaýaty            = models.ForeignKey(Welayatlar,on_delete=models.CASCADE)
    edarasy             = models.ForeignKey(Edaralar,on_delete=models.CASCADE)
    bölümi              = models.ForeignKey(Bolumler,on_delete=models.CASCADE)
    dokument            = models.FileField(upload_to='Dokumentler')
    görnüşi             = models.ForeignKey(Hasabat,on_delete=models.CASCADE)
    döredilen_senesi    = models.DateTimeField(auto_now=True)
    üýgedilen_senesi    = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural =("Faýl")
    def __str__(self):
        return self.ady