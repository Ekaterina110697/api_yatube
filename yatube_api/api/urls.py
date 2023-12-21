from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


ver1_router = routers.DefaultRouter()
ver1_router.register(r'posts', PostViewSet)
ver1_router.register(r'groups', GroupViewSet)
ver1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(ver1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
