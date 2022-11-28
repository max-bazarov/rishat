from django.urls import path

from .views import CancelView, ItemDetail, ItemList, StripeSession, SuccessView

urlpatterns = [
    path('buy/<int:pk>/', StripeSession.as_view(), name='buy'),
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]
