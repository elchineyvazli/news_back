from django.db import models
from django.contrib.postgres.fields import ArrayField


class ECards(models.Model):
    CATEGORY_CHOICES = [
        ('lifestyle', 'Lifestyle'),
        ('food_drinks', 'Food & Drinks'),
        ('technology', 'Technology'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
    ]

    e_title = models.CharField(max_length=200)
    e_desc = models.TextField()
    e_tag = ArrayField(
        models.CharField(max_length=30),
        default=list,
    )
    e_views_count = models.SmallIntegerField()

    class Meta:
        db_table = '"News"."ECards"'

    def __str__(self):
        return self.e_title


class TCards(models.Model):
    CATEGORY_CHOICES = [
        ('lifestyle', 'Lifestyle'),
        ('food_drinks', 'Food & Drinks'),
        ('technology', 'Technology'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
    ]

    url = models.CharField(max_length=200)
    t_title = models.CharField(max_length=60)
    t_desc = models.TextField()
    t_tag = ArrayField(
        models.CharField(max_length=30),
        default=list,
    )
    t_views_count = models.IntegerField()

    class Meta:
        db_table = '"News"."TCards"'

    def __str__(self):
        return self.t_title


class Comments(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = '"News"."Comments"'

    def __str__(self):
        return self.username
