from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Meetup(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    date = models.DateTimeField()
    image = models.ImageField(upload_to="meet_image", blank=True)
    slug = models.SlugField(default="", null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Address(models.Model):
    address = models.CharField(max_length=150)
    meetup = models.OneToOneField(
        to=Meetup, on_delete=models.CASCADE, related_name="address"
    )

    def __str__(self) -> str:
        return self.address


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    meet = models.ManyToManyField(to=Meetup, related_name="people")
