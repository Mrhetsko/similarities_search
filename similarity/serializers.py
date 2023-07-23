from rest_framework import serializers
from .models import Item, Search


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        return Item.objects.create(**validated_data)


class SearchItemRequest(serializers.Serializer):
    search_input = serializers.CharField(default='a postman')  # search input


class SearchItemResponse(serializers.Serializer):
    search_id = serializers.IntegerField(default=42)


class GetResultsRequest(serializers.Serializer):
    search_id = serializers.IntegerField(default=2)
    # search_item = Search.objects.get(pk=search_id)


class GetResultsResponse(serializers.Serializer):
    similarities = serializers.JSONField(default=[
    {
        "id": 1,
        "description": "This is from postman request"
    },
    {
        "id": 3,
        "description": "postman works hard"
    }])























