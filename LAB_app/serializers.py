from rest_framework.serializers import ModelSerializer

from LAB_app.models import NProducts, Shipment, HProducts, Contacts


class NProductsSerializer(ModelSerializer):
    class Meta:
        model = NProducts
        fields = (
        'id',
        'name',
        'price',
        'type',
        'formFactor'
        )

class ShipmentSerializer(ModelSerializer):
    class Meta:
        model = Shipment
        fields = (
        'formFactor',
        'method'
        )

class HProductsSerializer(ModelSerializer):
    class Meta:
        model = HProducts
        fields = (
        'id',
        'name',
        'price',
        'cal'
        )

class ContactsSerializer(ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
        'id',
        'organization',
        'post',
        'phone',
        'phone2',
        'email'
        )