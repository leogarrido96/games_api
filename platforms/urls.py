from django.urls import path
from platforms import views

urlpatterns = [
    path('platform/', views.PlatformListView.as_view(), name='platform-create-list'),
    path('platform/<int:pk>/', views.PlatformRetrieveUpdateDestroyView.as_view(), name='platform-detail'),

]
