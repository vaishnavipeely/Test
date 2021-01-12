from django.urls import path

from . import views
from .views import TestView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('api/',TestView.as_view(),name='test'),
    #path('api1/',TestView1.as_view(),name='test'),
    path('result/', views.result, name='result'),
    path('checkapi/',views.saveapi, name='saveapi'),
    # path('ge/', views.gett, name='result'),

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
