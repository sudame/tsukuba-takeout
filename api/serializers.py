from rest_framework import serializers
from food_tickets.models import Store, StoreArea, StoreGenre, StoreOpeningHour
from django.urls import reverse


class StoreAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreArea
        fields = "__all__"


class StoreGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreGenre
        fields = "__all__"


class StoreOpeningHourSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = StoreOpeningHour
        fields = ["opening_time", "closing_time", "id"]


class StoreSerializer(serializers.ModelSerializer):
    genres = StoreGenreSerializer(many=True, read_only=True)
    area = StoreAreaSerializer()
    opening_hours = StoreOpeningHourSeriaizer(many=True, read_only=True)
    url = serializers.SerializerMethodField()

    def get_url(self, url):
        return reverse("food_tickets:store", kwargs=dict(pk=u"1"))

    class Meta:
        model = Store
        fields = "__all__"
