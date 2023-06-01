from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('ad/', views.ad, name="user_login"),
    path('Dashboard/', views.signin, name="signin"),
    path('admin_dash/', views.admin, name="admin"),
    path('video_feed/', views.Live, name='video_feed'),
    path('Dashboard/punchin/', views.index1, name='stream_video'),
    path('Dashboard/punchout/', views.index2, name='stream_video'),
    path('register/', views.register, name='register'),
    path('up/', views.upreg, name='register'),
    #path("Dashboard/add_event/", views.add_event, name="update_datetime"),
]
