from django.db import models

class Task(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    heading = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading
    