from rest_framework import serializers
from .models import ECards, TCards, Comments


class ECardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECards
        fields = '__all__'


class TCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCards
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['username', 'message']
