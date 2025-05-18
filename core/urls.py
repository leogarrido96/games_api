from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('characters.urls')),
    path('api/v1/', include('developers.urls')),
    path('api/v1/', include('games.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('platforms.urls')),

]
