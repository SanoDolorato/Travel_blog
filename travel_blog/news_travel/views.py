from django.shortcuts import render

def post_list(request):
    return render(request, 'news_travel/post_list.html', {})