from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path(r"^__debug__/", include(debug_toolbar.urls))]
