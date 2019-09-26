from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='./media/profile_pics/one.png', upload_to='media/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.image.path)

        if image.height > 350 or image.width > 350:
            output_size = (350, 350)
            image.thumbnail(output_size)
            image.save(self.image.path)
