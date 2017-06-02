from django.shortcuts import render
from django.views import generic
from .models import content

# Create your views here.


def index(request):
    context = {}
    return render(request, 'aggregator/index.html', context)


class IndexView(generic.ListView):
    template_name = 'aggregator/index2.html'

    def get_queryset(self):
        return content.objects.all().filter(grade='5th')
