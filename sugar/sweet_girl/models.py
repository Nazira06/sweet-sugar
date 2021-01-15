from django.db import models

# Create your models here.
class Service(models.Model):
    categories = (
        ('ноги', 'ноги'),
        ('руки', 'руки'),
        ('лицо', 'лицо'),
    )

    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices=categories)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True, related_name='service')


class Master(models.Model):
    expr = (
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('master', 'master')
    )

    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=50)
    exp = models.CharField(max_length=50, choices=expr)


class Certificates(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True, related_name='certificate')


class Feedback(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)


