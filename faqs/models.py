from django.db import models

# Create your models here.

class Faqs(models.Model):
    question = models.CharField(
        max_length=255, unique=True, verbose_name="Question")
    answer = models.TextField(verbose_name="Answer")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['id']

    def __str__(self):
        return self.question
