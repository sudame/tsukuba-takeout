from rest_framework import serializers

from food_tickets.models import Store, StoreArea, StoreGenre


class StoreAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreArea
        fields = "__all__"


class StoreGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreGenre
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    genres = StoreGenreSerializer(many=True, read_only=True)
    area = StoreAreaSerializer()

    class Meta:
        model = Store
        fields = "__all__"
