#AyazSaiyed's - The Background Remover

from django.db import models

# Create your models here.

class users(models.Model):
	username = models.TextField(max_length=30)
	image = models.ImageField(upload_to='images',blank=False)
	useremail = models.EmailField(blank=True)
	userpassword = models.TextField()
	userphone = models.TextField(max_length=10)


	def __str__(self):
		return self.username


class imageupload(models.Model):
	usernamea = models.TextField(max_length=30)
	uploadedimage = models.ImageField(upload_to='uploadedimages',blank=False)



