from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='link-detail', lookup_field='slug')

    class Meta:
        model = Link
        fields = ('name', 'url', 'creation_time', 'link', 'slug')
