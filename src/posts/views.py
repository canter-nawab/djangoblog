from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
	form=PostForm(request.POST or None)
	if form.is_valid():
		instance =form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
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
	queryset_list=Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
    	queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
    	queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    	queryset = paginator.page(paginator.num_pages)
	context={
		"object_list":queryset,
		"title":"List"
	}
	return render(request,"post_list.html",context)





	#return HttpResponse("<h1>List</h1>")
def post_update(request, id =None):
	instance=get_object_or_404(Post,id=id)
	form=PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance =form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>post</a> Saved....",extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request,"post_form.html",context)

	
def post_delete(request,id =None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")
