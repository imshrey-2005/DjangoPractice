from django.db import models

# Create your models here.
class Tour(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")

    def __str__(self):
        return f"{self.origin} to {self.destination} - {self.duration} days at ${self.price}"

    