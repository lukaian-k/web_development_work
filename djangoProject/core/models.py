from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    # Criação do usuário
    def create_user(self, id_user, password=None):
        if not id_user:
            raise ValueError("O campo 'id_user' é obrigatório.")

        user = self.model(id_user=id_user)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_user, password=None):
        user = self.create_user(id_user, password=password)
        user.is_staff = True
        user.id_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    id_user = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'id_user'

    def __str__(self):
        return self.id_user