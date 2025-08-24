from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_artist', 'is_gallery']
        read_only_fields=['id']

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'website', 'profile_picture', 'phone_number']

class Social_linkSerializer(ModelSerializer):
    class Meta:
        model = Social_links
        fields = ['platform', 'url', 'profile_picture', 'phone_number']

class UserProfileSerialier(ModelSerializer):
    profile= ProfileSerializer()
    social_links = Social_linkSerializer(many=True, read_only=True)

    class Meta:
        model=User
        fields=['id', 'username', 'email', 'is_artist', 'is_gallery', 'profile', 'social_links']
        read_only_fields = ['id', 'username', 'email', 'is_artist', 'is_gallery']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        social_links_data = validated_data.pop('social_links', [])
        user = User.objects.create(**validated_data)
        profile = Profile.objects.create(user=user, **profile_data)
        
        for social_link_data in social_links_data:
            Social_links.objects.create(profile=profile, **social_link_data)

        return user