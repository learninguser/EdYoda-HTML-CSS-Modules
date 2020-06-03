from django.urls import path
from blog import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:id>',views.post_details),
]