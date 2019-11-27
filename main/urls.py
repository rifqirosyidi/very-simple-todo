from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^add_todo/', views.add_todo, name='add'),
  url(r'^del_todo/(?P<todo_id>\d+)/', views.del_todo, name='del'),
]
