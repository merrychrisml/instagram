from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(validators=[MinLengthValidator(10)])
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.message} by {self.author}"