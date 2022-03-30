from django.urls import path, include
from . import views
# from manage_docs.views import UserViewSet
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
#
urlpatterns = [
    # path('', include(router.urls)),
    path('folders/', views.folders_list),
    path('folders/<int:pk>/', views.folders_detail),
    # path('docs/', views.doc_list),
    path('docs/', views.doc_detail),
    # path('docs/<str:folders>/', views.doc_detail),
    path('topics/', views.topics_list),
    path('topics/<int:pk>/', views.topics_detail),
]