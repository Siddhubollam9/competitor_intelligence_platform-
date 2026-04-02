from rest_framework import serializers
from .models import Competitor, ScrapedUpdate


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = "__all__"


class ScrapedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedUpdate
        fields = "__all__"