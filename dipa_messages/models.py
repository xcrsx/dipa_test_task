from django.db import models


class MessageModel(models.Model):
    email = models.EmailField(max_length=150, default="anonym@dipa.ru")
    message = models.CharField(max_length=250, default="")

    def __str__(self):
        return f"sender: {self.email}, the message: {self.message}"
