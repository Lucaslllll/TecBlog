from django.db import models
from django.contrib.auth.models import User

# comentários
# artigo
# tem que criar uma conta para fazer comentários
# texto longo e o texto pequeno para colocar na lista
# só 10 os mais recentes na página inicial 
# contos de empreendedorismo e com lições
# dividir em paragráfos o texto
# anuncios
#
#page pesquisa
#page registro
#
# 
# 
# Django
# Pillow
# 

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/foto_users', blank=True, null=True)
    logged = models.BooleanField(null=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    resume = models.CharField(max_length=255, help_text=('Texto curto com 255 caracteres para listar.'))
    paragraphs = models.TextField()
    image = models.ImageField(upload_to='media/foto_article', null=True)
    date_send = models.DateField(auto_now_add=True)
    date_update = models.DateField(null=True, blank=True)
    is_visible = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    details = models.TextField() 
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, blank=True)
    date_send = models.DateField(auto_now_add=True, null=True)

class Recomment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    own = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    details = models.TextField()
    likes = models.IntegerField(null=True, blank=True)
    date_send = models.DateField(auto_now_add=True, null=True)

class Ads(models.Model):
    image = models.ImageField(upload_to='media/foto_ads', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=10000)
    is_visible = models.BooleanField(null=True, default=True)