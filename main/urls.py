from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("lists/", views.lists, name="lists"),
    path("category/<str:c2>/", views.category, name="category"),
    path("new/", views.new, name="new"),
    path("search/", views.search, name = "search"),
    path("list/item/<int:pk>", views.item, name="item"),
    path("list/item/<int:pk>/use/", views.use, name="use"),
    path("list/item/<int:pk>/<str:date>/<str:number>/<str:b_or_n>/", views.b_or_n, name="b_or_n"),
]