from .import views
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('', views.index),

    path('api/add_item/', views.add_item),
    path('api/search_similarities/', views.search_items),
    path('api/get_search_results/', views.get_search_results),

    # docs
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='api_docs'),

]
