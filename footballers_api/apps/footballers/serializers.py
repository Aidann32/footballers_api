from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Footballer, Country, FootballClub, FootballerImage


class FootballerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballerImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

class FootballClubSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=False)

    class Meta:
        model = FootballClub
        fields = ('country', 'name')


class FootballerSerializer(serializers.ModelSerializer):
    club = FootballClubSerializer()
    images = FootballerImageSerializer(source='footballerimage_set', many=True)
    
    class Meta:
        model = Footballer
        fields = ('first_name', 'last_name', 'club', 'shirt_number', 'date_of_birth', 'bio', 'images')
        