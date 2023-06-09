from django.urls import path
from posts.views import feeds, post_add, comment_add, comment_delete, tags, post_detail

app_name = 'posts'
urlpatterns = [
    path('feeds', feeds, name='feeds'),
    path('post_add', post_add, name='post_add'),
    path('comment_add', comment_add, name='comment_add'),
    path('comment_delete/<int:comment_id>',
         comment_delete, name='comment_delete'),
    path('tags/<str:tag_name>', tags, name='tags'),
    path('<int:post_id>', post_detail, name='post_detail'),
]
