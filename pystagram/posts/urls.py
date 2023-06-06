from django.urls import path
from posts.views import feeds, post_add, comment_add, comment_delete

app_name = 'posts'
urlpatterns = [
    path('feeds', feeds, name='feeds'),
    path('post_add', post_add, name='comment_add'),
    path('comment_add', comment_add, name='comment_delete'),
    path('comment_delete/<int:comment_id>', comment_delete, name='post_add')
]
