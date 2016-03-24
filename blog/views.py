from django.shortcuts import render
from django.utils import timezone
# to add some info from our DB and add some dynamic in content we neew to connect our DB ot template
# that is why we add next line. W/o it we display just static content written by hands
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})
	# {} - here we put what we gonna use in our template to connect
	# model and template. We want to display posts from our DB so we use 'posts'
