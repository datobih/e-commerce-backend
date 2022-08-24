from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

# Create your models here.
class ActivationToken(models.Model):
    token=models.CharField(max_length=6)
    user=models.OneToOneField(User,related_name='activation_token',on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user.email}'s token"