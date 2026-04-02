from django.db import models


class Competitor(models.Model):
    name = models.CharField(max_length=120)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ScrapedUpdate(models.Model):
    competitor = models.ForeignKey(
        Competitor,
        on_delete=models.CASCADE,
        related_name="updates"
    )

    title = models.CharField(max_length=300)
    link = models.URLField()
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title