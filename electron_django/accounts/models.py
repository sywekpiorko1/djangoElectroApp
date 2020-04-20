from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # override default behaviour of save() to resize profile picture size
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # get image of current instance
        img = Image.open(self.image.path)

        # we resize picture over 300 pixels height or width
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
