from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'itservice1/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'itservice1/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'itservice1/topic.html', context)


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'itservice1/results.html', {'error_msg': error_msg})
    else:
        post_list = Entry.objects.filter(title__icontains=q)
        return render(request, 'itservice1/results.html', {'error_msg': error_msg, 'post_list': post_list})
