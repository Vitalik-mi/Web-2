from django.db import models
import os
from PIL import Image

class Product(models.Model):
	PROSTHESIS = 'prosthesis'
	EXOSCELETION ='exosceletion'
	REABILITATION = 'reabilitation'
	ACC = 'Accessories'

	CHOICE_GROUP = {
		('P', 'prosthesis'),
		('E', 'exosceletion'),
		('R', 'reabilitation'),
		('A', 'Accessories'),
	}

	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField()
	availability = models.BooleanField(default=True)
	group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=PROSTHESIS)
	img = models.ImageField(default='noimage.jpg', upload_to='product_image')


	def __str__(self):
		return f'{self.name}'

