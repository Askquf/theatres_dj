from main_app.models import Theatre, District, Perfomance
from rest_framework import serializers

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ["url", "name", "id", "information", "image_source", "district_id"]

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["name", "id"]

class PerfomanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfomance
        fields = ["name", "information", "image_source", "id", "theatre_url"]
