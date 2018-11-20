from django.shortcuts import render

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin

from rest_framework import viewsets

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from rest_framework.viewsets import GenericViewSet


from LAB_app.models import NProducts, Shipment, HProducts, Contacts
from LAB_app.serializers import NProductsSerializer, ShipmentSerializer, HProductsSerializer, ContactsSerializer

def GetNPInfo(request):
    products = NProducts.objects.all()
    str1 = ''
    i = 1
    for per in products:
        str1 += '<h3>NProducts' + str(i) + '</h3>'
        str1 += '<p>ID: ' + per.id + '</p>'
        str1 += '<p>NAME: ' + per.name + '</p>'
        str1 += '<p>Price: ' + per.price + '</p>'
        str1 += '<p>Type: ' + per.type + '</p>'
        str1 += '<p>FormFactor: ' + per.formFactor + '</p>'
        i += 1

    return HttpResponse(str1)

def product_view(request, pk, template_name='site/table.html'):
    product = get_object_or_404(NProducts, pk=pk)
    return render(request, template_name, {'product':product})

class NProductsViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin
):
    serializer_class = NProductsSerializer
    queryset = NProducts.objects.all()

class ShipmentViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin
):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

class HProductsViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin
):
    serializer_class = HProductsSerializer
    queryset = HProducts.objects.all()

class ContactsViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin
):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

class NProductsViewSet(viewsets.ViewSet):
    @staticmethod
    def get(request):
        template = 'site/table.html'
        nproducts = NProducts.objects.all()
        return render(request, template, {'nproducts': nproducts})

class ShipmentViewSet(viewsets.ViewSet):
    @staticmethod
    def get(request):
        template = 'site/table.html'
        shipment = Shipment.objects.all()
        return render(request, template, {'shipment': shipment})

class HProductsViewSet(viewsets.ViewSet):
    @staticmethod
    def get(request):
        template = 'site/table.html'
        hproducts = HProducts.objects.all()
        return render(request, template, {'hproducts': hproducts})

class ContactsViewSet(viewsets.ViewSet):
    @staticmethod
    def get(request):
        template = 'site/table.html'
        contacts = Contacts.objects.all()
        return render(request, template, {'contacts': contacts})