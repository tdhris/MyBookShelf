from django.shortcuts import render, get_object_or_404, redirect
from forums.models import Forum, Topic, Post
from forums.forms import AddTopicForm, AddPostForm


def home_forums(request):
    forums = Forum.objects.all()
    user = request.user
    return render(request, 'index.html', locals())


def view_forum(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    return render(request, 'view_forum.html', locals())


def add_forum(request):
    pass


def new_topic(request, forum_id):
    form = AddTopicForm()
    return render(request, 'add_topic.html', locals())


def add_topic(request, forum_id):
    form = AddTopicForm(data=request.POST)
    if form.is_valid():
        for_forum = get_object_or_404(Forum, pk=forum_id)
        poster = form.cleaned_data.get('creator')
        new_topic = Topic.objects.create(title=form.cleaned_data.get('title'),
                                         creator=poster,
                                         forum=for_forum,
                                         date_created=form.cleaned_data.get('date_created'))
        create_first_post(new_topic, poster,
                          form.cleaned_data.get('first_topic_text'))
        return redirect(new_topic)
    else:
        return render(request, 'view_forum.html', locals())


def view_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'view_topic.html', locals())


def create_first_post(new_topic, user, topic_text):
    new_post = Post.objects.create(text=topic_text,
                                   poster=user,
                                   topic=new_topic)
    new_post.save()


def reply(request, topic_id):
    form = AddPostForm()
    return render(request, 'reply.html', locals())


def post_reply(request, topic_id):
    form = AddPostForm(data=request.POST)
    if form.is_valid():
        for_topic = get_object_or_404(Topic, pk=topic_id)
        reply = Post.objects.create(text=form.cleaned_data.get('text'),
                                    date_created=form.cleaned_data.get('date_created'),
                                    poster=form.cleaned_data.get('poster'),
                                    topic=for_topic)
        return redirect(for_topic)
    else:
        return render(request, 'view_topic.html', locals())
