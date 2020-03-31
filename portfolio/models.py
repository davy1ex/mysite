from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    description = models.CharField(max_length=100)
    github_link = models.CharField(max_length=64)


class DesktopImage(models.Model):
    project = models.ForeignKey(Project, related_name="desktop_images", on_delete=models.CASCADE)
    image = models.ImageField()