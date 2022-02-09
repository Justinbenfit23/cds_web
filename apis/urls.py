from django.urls import path
from .views import CMCView

urlpatterns = [
    path('', CMCView.as_view())

]