from django.shortcuts import render, HttpResponse
from django.views import generic


from .models import chapterDetail

# Create your views here.


def index(request):
    context = {}
    return render(request, 'aggregator/index.html', context)


def chapter(request):
    return HttpResponse("{% csrf_token %}<h3>Hello!</h3>")


class IndexView(generic.ListView):
    model = chapterDetail
    template_name = 'aggregator/textbook.html'


    def get_queryset(self):
        queryset = chapterDetail.objects.all()

        if self.request.GET.get('grade'):
            queryset = queryset.filter(grade=self.request.GET.get('grade'))
        return queryset
