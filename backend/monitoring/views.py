from rest_framework import generics
from .models import Competitor, ScrapedUpdate
from .serializers import CompetitorSerializer, ScrapedUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScrapedUpdate
from .ai_analyzer import analyze_updates, generate_recommendations

class CompetitorListCreateView(generics.ListCreateAPIView):
    queryset = Competitor.objects.all()
    serializer_class = CompetitorSerializer


class ScrapedUpdateListView(generics.ListAPIView):
    queryset = ScrapedUpdate.objects.all()
    serializer_class = ScrapedUpdateSerializer
    
class AnalysisView(APIView):
    def get(self, request):
        updates = ScrapedUpdate.objects.all()

        insights = analyze_updates(updates)
        recommendations = generate_recommendations(insights)

        return Response({
            "insights": insights,
            "recommendations": recommendations
        })