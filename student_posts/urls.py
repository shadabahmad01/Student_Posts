from . import views
from django.urls import path

app_name = 'student_posts'
urlpatterns = [
	path('', views.index, name='home'),
	path('blogs/', views.PostList, name='blogs'),
	path('blogs/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
	path('new_post/', views.new_post, name='new_post'),
	path('user_post/', views.user_post, name='user_post'),
	path('explist/', views.ExpList, name='explist'),
	path('expdetail/<slug:slug>/', views.ExpDetail.as_view(), name='expdetail'),
	path('new_exp/', views.new_exp, name='new_exp'),
	path('user_exp/', views.user_exp, name='user_exp'),
	path('prompt/', views.prompt, name="prompt"),
]