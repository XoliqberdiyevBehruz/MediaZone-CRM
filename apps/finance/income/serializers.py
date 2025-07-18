from django.db import transaction

from rest_framework import serializers 

from apps.finance.models import Income, IncomeCategory


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = [
            'id', 'name', 'total_price'
        ]


class IncomeCreateSerializer(serializers.Serializer):
    category_id = serializers.UUIDField()
    price = serializers.IntegerField()
    date = serializers.DateField()
    comment = serializers.CharField(required=False)

    def validate(self, data):
        try:
            category = IncomeCategory.objects.get(id=data.get('category_id'))
        except IncomeCategory.DoesNotExist:
            raise serializers.ValidationError("category not found")
        data['category'] = category
        return data 
    
    def create(self, validated_data):
        with transaction.atomic():
            expence = Income.objects.create(**validated_data)
            return expence
        return None


class IncomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        