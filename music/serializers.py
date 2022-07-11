from rest_framework import serializers

# from music.models import Selection
#
#
# class SelectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Selection
#         fields = '__all__'
#
from music.models import Track, Selection
from user.serializers import UserSerializer


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        read_only_fields = ('id',)
        fields = (
            'id',
            'name',
            'author',
            'release_date',
            'genre',
            'duration_in_seconds',
            'album',
            'logo',
        )


class StaredTrackSerializer(serializers.ModelSerializer):
    stared_user = UserSerializer(many=True)

    class Meta:
        model = Track
        read_only_fields = ('id',)
        fields = (
            'id',
            'name',
            'logo',
            'stared_user',
        )


class AddToFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Track
        fields = (
            'id',
            "name",
            'user',
        )


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = TrackSerializer(many=True)
    owner = serializers.SlugRelatedField(
        slug_field="email",
        read_only=True,
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
