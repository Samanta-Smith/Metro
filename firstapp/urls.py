from django.urls import path
from .views import ArticleView
app_name = "firstapp"
urlpatterns = [
    path('v1/metro/verificate', ArticleView.as_view()),
]
