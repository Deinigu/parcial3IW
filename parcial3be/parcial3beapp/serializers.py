from rest_framework import serializers

class PruebaSerializer(serializers.Serializer):

    _id = serializers.CharField(max_length = 24, required=False)
    nombre = serializers.CharField()
    timestamp = serializers.DateTimeField(required=False)
    lugar = serializers.CharField()
    lat = serializers.FloatField(required = False)
    lon = serializers.FloatField(required = False)
    organizador = serializers.CharField()
    imagen = serializers.CharField()
    
class TokenSerializer(serializers.Serializer):
    idtoken = serializers.CharField()
