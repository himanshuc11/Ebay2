from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-item/', views.create_item, name="create_item"),
    path('detailed-item/<int:id>', views.detailed_view, name="detailed_view"),
    path('close-auction/<int:id>', views.close_auction, name="close_auction")
]
