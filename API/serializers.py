from rest_framework import serializers
from main.models import Data, Region, Country,Sector,Pestle,Source,Topic

class DataSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()
    sector = serializers.StringRelatedField()
    topic  = serializers.StringRelatedField( read_only=True)
    region  = serializers.StringRelatedField( read_only=True)
    country  = serializers.StringRelatedField( read_only=True)
    pestle  = serializers.StringRelatedField( read_only=True)
    source  = serializers.StringRelatedField( read_only=True)

    class Meta: 
        model = Data
        fields = '__all__'
        

class RegionSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Region
        fields = '__all__'
        

class CountrySerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Country
        fields = '__all__'
        

class SectorSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Sector
        fields = '__all__'
        

class PestleSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Pestle
        fields = '__all__'
        

class SourceSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Source
        fields = '__all__'
        

class TopicSerializer(serializers.ModelSerializer):

    # id = serializers.ReadOnlyField()

    class Meta: 
        model = Topic
        fields = '__all__'
        