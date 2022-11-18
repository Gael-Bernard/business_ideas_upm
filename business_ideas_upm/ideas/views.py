from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import BusinessIdea

# Create your views here.

def list(request):
    ideas_list = BusinessIdea.objects.order_by("-publish_date")[:10]
    template = loader.get_template('ideas/list.html')
    context = {
        'ideas_list': ideas_list,
    }
    return HttpResponse(template.render(context, request))


def idea(request, idea_id):
    try:
        idea = BusinessIdea.objects.get (pk=idea_id)
    except BusinessIdea.DoesNotExist:
        raise Http404("Idea does not exist")
    return render(request, 'ideas/detail.html', {"idea": idea})