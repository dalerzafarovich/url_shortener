from django.db import models, IntegrityError
from django.utils.crypto import get_random_string
from string import ascii_letters, digits


class Link(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(unique=True, blank=True, null=True)

    link = models.URLField()

    @staticmethod
    def generate_url():
        characters = ascii_letters + digits
        result = get_random_string(8, characters)
        return result

    def save(self, *args, **kwargs):
        try:
            if not self.slug:
                self.slug = self.generate_url()
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)
