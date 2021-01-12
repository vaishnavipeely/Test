from rest_framework import serializers
from .models import Apimodel



class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apimodel
        fields = ['id', 'Quiz', 'sampletest','sleeping','learning','playing']