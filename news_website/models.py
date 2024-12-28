from django.db import models


class News(models.Model):
    CATEGORY_CHOICES = [
        ('lifestyle', 'Lifestyle'),
        ('food_drinks', 'Food & Drinks'),
        ('technology', 'Technology'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    tag = models.CharField(max_length=20)

    class Meta:
        db_table = 'EditorsPicks'

    def __str__(self):
        return self.title
