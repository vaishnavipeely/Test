from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('result/', views.result, name='result'),
    # path('ge/', views.gett, name='result'),

    #path('api/',views.api, name='api'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
