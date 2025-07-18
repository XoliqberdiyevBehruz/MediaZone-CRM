from django.db import models

from apps.shared.models import BaseModel


class Partner(BaseModel):
    icon = models.FileField(upload_to='media_zone/partners')
    instagram_link = models.URLField(null=True, blank=True)

class Image(BaseModel):
    image = models.ImageField(upload_to='media_zone/images')

class Video(BaseModel):
    video = models.FileField(upload_to="media_zone/videos")


class Team(BaseModel):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media_zone/teams")

