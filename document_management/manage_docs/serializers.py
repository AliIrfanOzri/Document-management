from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class FoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folders
        fields = "__all__"


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digital_Documents
        # fields = "__all__"
        exclude = ['i_folders']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = "__all__"

