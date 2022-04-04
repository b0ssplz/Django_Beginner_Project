from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index, name='posts_home'),
    path('greet/',views.greet, name='greet_name'),
    # path('posts/',views.return_all_posts, name='all_posts'),
    # path('post/<int:post_id>',views.return_one_post, name='one_post'),
    path('about/',views.about, name='posts_about'),
    path('services/',views.services, name='posts_services'),
    path('create_post/',views.create_post, name='create_post'),
    path('post/<int:post_id>',views.post_detail, name='post_detail'),
    path('post/update/<int:post_id>',views.update_post, name='update_post'),


]
