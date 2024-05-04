from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    

class RequestBody(serializers.Serializer):
    
    Seed_RepDate =  serializers.IntegerField()
    Seed_Year = serializers.IntegerField()
    Seeds_YearWeek = serializers.IntegerField()
    Seed_Varity =  serializers.CharField()
    Seed_RDCSD = serializers.CharField()
    Seed_Stock2Sale = serializers.IntegerField()
    Seed_Season = serializers.IntegerField()
    Seed_Crop_Year =  serializers.CharField()
