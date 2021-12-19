from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from core.utils.cryptography import encryption, decryption
# Create your models here.

class Door(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10,
        choices=(
            ("open", "Open"),
            ("close", "Close"),
        )
    )
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('door-status', kwargs={
            'id': self.id
        })

    def save(self, *args, **kwargs):
        self.password = encryption(self.password)
        super(Door, self).save(*args, **kwargs)

    def check_password(self, password):
        """check password is true"""
        return password == decryption(self.password)

