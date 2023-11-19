from django.urls import path, include
from API import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('',include(router.urls)),

    # path('', views.DataViewSet, name='all data'),
]


