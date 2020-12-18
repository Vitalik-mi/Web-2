from django.shortcuts import render
from web.models import Product


def index(reguest):
	return render(reguest, 'web/index.html')



def shop(reguest):
	product = Product.objects.all()
	context = {
		'pr': product
	}
	return render(reguest, 'web/shop.html', context)

