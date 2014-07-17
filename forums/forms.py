from django import forms
from forums.models import Forum, Topic, Post


class AddTopicForm(forms.models.ModelForm):
    first_topic_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Topic
        exclude = ['forum']


class AddForumForm(forms.models.ModelForm):
    class Meta:
        model = Forum


class AddPostForm(forms.models.ModelForm):
    class Meta:
        model = Post
        exclude = ['topic']
