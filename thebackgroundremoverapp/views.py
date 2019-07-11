from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
from .models import users,imageupload
from removebg import RemoveBg



def index(request):
	return render(request,'thebackgroundremoverapp/index.html')

def generic(request):
	return render(request,'thebackgroundremoverapp/generic.html')

def elements(request):
	return render(request,'thebackgroundremoverapp/elements.html')

def signup(request):
	return render(request,'thebackgroundremoverapp/signup.html')

def login(request):
	return render(request,'thebackgroundremoverapp/login.html')

def signupdetails(request):
	un = request.POST.get('name')
	ue = request.POST.get('email')
	up = request.POST.get('phone')
	upwd = request.POST.get('password')
	img = request.FILES['img']
	fs = FileSystemStorage('./media/images/')
	filename = fs.save(img.name,img)

	users.objects.create(username=un,useremail=ue,userphone=up,userpassword=upwd)
	# return HttpResponse("Wooo you have successfully Registered")
	return render(request,'thebackgroundremoverapp/login.html')

def loginvalid(request):
	u = request.POST.get('username')
	p = request.POST.get('password')
	data = users.objects.all()
	for i in data:
		if i.username == u and i.userpassword == p:
			# a = i.image
			c = i.username
			request.session['username'] = c
			a = users.objects.filter(username=c)
			b = i.username
			# return HttpResponse("Login Success")
			return render(request,'thebackgroundremoverapp/elements.html',{'user':b,'userdetails':a})
	return HttpResponse("LOL")

	
def removebg(request):
	img = request.FILES['nimg']
	aa = request.session['username']
	fs = FileSystemStorage('./media/images/')
	filename = fs.save(aa,img)
	# a = str(i)
	rmbg = RemoveBg("jvcu8BVqELyUYURc99sfQbAb", "error.log")
# myimg = args["--image"]
	a = './media/images/'+aa
	rmbg.remove_background_from_img_file(a)
	b = './media/images/'+aa+'_no_bg.png'
	image_data = open('./media/images/'+aa+'_no_bg.png', "rb").read()
	return HttpResponse(image_data, content_type="image/png")

	# return HttpResponse("Done")



