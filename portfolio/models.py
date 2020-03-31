from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Project(models.Model):
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    description = models.CharField(max_length=100, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    
    # mobile_photo = models.ImageField(max_length=256)
    # mobile_photo = ArrayField(
    #     ArrayField(
    #         models.ImageField(max_length=64, blank=True),
    #     )
    # )

class DesktopImage(models.Model):
    project = models.ForeignKey(Project, related_name="desktop_images", on_delete=models.CASCADE)
    image = models.ImageField()
