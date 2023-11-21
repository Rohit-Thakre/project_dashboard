from rest_framework.serializers import ModelSerializer
from main.models import Data



class DataS(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'