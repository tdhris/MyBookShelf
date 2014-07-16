from django.contrib import admin
from forums.models import Forum, Topic, Post


class ForumAdmin(admin.ModelAdmin):
    pass


class TopicModerator(admin.ModelAdmin):
    pass


class PostModerator(admin.ModelAdmin):
    pass


admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicModerator)
admin.site.register(Post, PostModerator)
