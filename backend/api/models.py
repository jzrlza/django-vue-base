from django.db import models
from rest_framework import serializers
from django.core.validators import MinLengthValidator


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=25, validators=[MinLengthValidator(8)])
    def __str__(self):
        return self.username
