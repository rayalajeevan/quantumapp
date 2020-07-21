from rest_framework import serializers
from .models import Survey


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"

    def create(self, validated_data, *args, **kwrgs):
        return Survey.objects.create(**validated_data)
