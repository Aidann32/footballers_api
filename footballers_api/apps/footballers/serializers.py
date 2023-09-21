from rest_framework import serializers

from .models import Footballer, Country, FootballClub


class FootballClubSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=False)

    class Meta:
        model = FootballClub
        fields = ('country', 'name')


class FootballerSerializer(serializers.ModelSerializer):
    club = FootballClubSerializer()
    
    class Meta:
        model = Footballer
        fields = ('first_name', 'last_name', 'club', 'shirt_number', 'date_of_birth')
        