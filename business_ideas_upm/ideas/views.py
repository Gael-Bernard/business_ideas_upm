from django.http import HttpResponse
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
    return HttpResponse("Page of business idea "+str(idea_id))