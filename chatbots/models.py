from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField


class Chat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = HTMLField()
    response = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
