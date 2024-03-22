from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    movie_logo = models.FileField()

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)

class UsuarioModel:
    def __init__(self, id=0, senha="senha", email="email"):
        self.id = id
        self.senha = senha
        self.email = email

    def __eq__(self, other):
        if isinstance(other, UsuarioModel):
            return self.id == other.id and self.senha == other.senha and self.email == other.email
        return False

    def __hash__(self):
        return hash((self.id, self.senha, self.email))

    def __str__(self):
        return f"Usuário: id={self.id}, email={self.email}"

    # Método para representação mais amigável quando imprimir o objeto
    def __repr__(self):
        return self.__str__()

    # Getters
    def get_id(self):
        return self.id

    def get_senha(self):
        return self.senha

    def get_email(self):
        return self.email

