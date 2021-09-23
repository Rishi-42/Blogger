from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from os import stat

urlpatterns = [
    path('' , include('home.urls')),
    path('api/' , include('home.urls_api')),
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls'))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()