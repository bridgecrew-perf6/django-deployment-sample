from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    # create relationship (don't inherit from user)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", null=True)


    # add any additional attribute if u want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username