from django.shortcuts import render

def index(request):
  return render(request, 'blogs/index.html')


def post_details(request):
  return render(request, 'blogs/post_detail.html')


