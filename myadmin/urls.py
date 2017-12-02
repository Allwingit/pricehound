from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.update_price, name='update_price'),
]
