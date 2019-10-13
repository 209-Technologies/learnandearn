from django.shortcuts import render
from .models import DashboardCards
from .apps import DashboardConfig

app_name = DashboardConfig.name

# Index file
def index(request):
    dashboard_cards = DashboardCards.objects.all()
    return render(request, 'index.html', {'dashboard_cards':dashboard_cards, 'title':app_name})