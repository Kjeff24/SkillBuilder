from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import Http404
from .views import custom_404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path("", include("course.urls")),
    path("", include("quiz.urls")),
    re_path(r'^.*/$', custom_404),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)