"""
    DRF Serializers
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Placeholder

User = get_user_model()


class PlaceholderSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Placeholder
        fields = ('id', 'name', 'description', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('placeholder-detail', kwargs={'pk': obj.pk}, request=request)
        }


class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('user-detail', kwargs={'pk': obj.pk}, request=request)
        }