from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view()),
    re_path(r'^menu/items/(?P<pk>\d+)$', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
