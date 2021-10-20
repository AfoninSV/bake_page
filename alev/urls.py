from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from examples import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", vw.ex_list, name='c_list'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)