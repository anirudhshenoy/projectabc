from django.shortcuts import render, HttpResponse
from django.views import generic


from .models import content

# Create your views here.


def index(request):
    context = {}
    return render(request, 'aggregator/index.html', context)


def chapter(request):
    return HttpResponse("{% csrf_token %}<h3>Hello!</h3>")


class IndexView(generic.ListView):
    model = content
    template_name = 'aggregator/index2.html'

    # def post(self, request, *args, **kwargs):
    #     gradeRequest = request.POST.get('grade')
    #     subjectRequest = request.POST.get('subject')
    #     return HttpResponse(gradeRequest + ' ' + subjectRequest)

        #return HttpResponse(grade + ' ' + subject)
        #return render(request, self.template_name, {'gradeRequest': gradeRequest, 'subjectRequest': subjectRequest})

    def get_queryset(self):
        queryset = content.objects.all()

        if self.request.GET.get('grade'):
            queryset = queryset.filter(grade=self.request.GET.get('grade'))
        return queryset
