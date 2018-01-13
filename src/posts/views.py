from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):#basically retreive
	instance=get_object_or_404(Post,id=4)
	context={
		"title": "Detail"
	}
	return render(request,"index.html",context)

def post_list(request):# items in the list
	#if request.user.is_authenticated():
	#	context={
	#		"title":" My UserList"
	#	4
	#else:
	#	context={
	#		"title":"List"
	#	}
	queryset=Post.objects.all()
	context={
			"object_list":queryset,
			"title":"List"
	}
	return render(request,"index.html",context)
	#return HttpResponse("<h1>List</h1>")
def post_update(request):
	return HttpResponse("<h1>Update</h1>")
def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
