from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Conversation(models.Model):
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prompt}: {self.response}"
