# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django. db. models import Q
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import Order
# Create your views here.
@api_view(['POST','PUT','DELETE'])
def CreateOrder(request):
	if request.method=='POST':
		order_data=Order.objects.create(quantity=request.data['quantity'],product_id_id=request.data['product_id'])
		order_data.save()
		get_data=Order.objects.all()
		return Response(get_data)
	if request.method=='PUT':	
		get_order_id=Order.objects.select_related().get(product_id_id=request.data['id'])
		get_order_id.quantity=request.data['quantity']
		get_order_id.save()
		get_data=Order.objects.all()
		return Response(get_data)
	if request.method=='DELETE':
		get_order_id=Order.objects.get(product_id_id=request.data['id']).delete()
		get_data=Order.objects.all()
		return Response(get_data)
@api_view(['GET'])
def GetProduct(request):
	if request.method=='GET':
		get_product_instance=Product.objects.select_related().get(id=request.GET.get('id'))
		get_recommended_product=Product.objects.select_related().filter(Q(product_type=get_product_instance.product_type),Q(seasonal=get_product_instance.seasonal),Q(brand_id_id=get_product_instance.brand_id_id)).values('name','product_description','price','product_type','seasonal','brand_id')
		return Response(get_recommended_product)