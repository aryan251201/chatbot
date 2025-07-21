from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, AskView

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ask/', AskView.as_view(), name='ask-question'),
]