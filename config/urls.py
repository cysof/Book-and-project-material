from django.conf import settings # new
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('anything-but-admin/', admin.site.urls),
# User management
    path('accounts/', include('allauth.urls')),
# Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')), # new
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns