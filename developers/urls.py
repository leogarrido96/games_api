from django.urls import path 

from developers.views import DeveloperListView, DeveloperRetrieveUpdateDestroyView


urlpatterns = [
    path('developers/', DeveloperListView.as_view(), name='developer-create-list'),
    path('developers/<int:pk>/', DeveloperRetrieveUpdateDestroyView.as_view(), name='developer-detail'),
]