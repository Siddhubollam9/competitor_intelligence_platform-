from django.urls import path
from .views import CompetitorListCreateView, ScrapedUpdateListView
from .views import AnalysisView

urlpatterns = [
    path("competitors/", CompetitorListCreateView.as_view()),
    path("updates/", ScrapedUpdateListView.as_view()),
    path("analysis/", AnalysisView.as_view()),
]