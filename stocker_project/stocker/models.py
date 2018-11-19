from django.db import models
#from django.contrib.auth.models import User

class Unidade(models.Model):
    nome = models.CharField(max_length=128)
    def __str__(self):
        return self.nome


class Insumo(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    quantidade = models.IntegerField(default=0)
    ativo = models.BooleanField(default=1)
    data = models.DateField(auto_now=True)
    unidade = models.ForeignKey(Unidade, blank=True, null=True)
    def __str__(self):
        return self.nome


#class UserProfile(models.Model):
#    user = models.OneToOneField(User)
#    website = models.URLField(blank=True)
#    picture = models.ImageField(upload_to='profile_images', blank=True)
#
#    def __str__(self):
#        return self.user.username