from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance =form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
	#if request.method == "POST":
		#print "title" + request.POST.get("content")
		#print request.POST.get("title")
		#Post.objects.create(title = title)
	context={ 
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request, id=None):#basically retreive
	instance=get_object_or_404(Post,id=id)
	context={
		"title":instance.title,
		"instance":instance,
	}
	return render(request,"post_detail.html",context)

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
