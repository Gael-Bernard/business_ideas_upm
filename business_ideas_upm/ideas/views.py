from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

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
    
    #comments = IdeaComment.objects.filter()
    print(idea.__dir__())
    return render(request, 'ideas/detail.html', {"idea": idea, "comments": ""})


def idea_new(request):
    return render(request, "ideas/idea_new.html")


def idea_new_post(request):
    print(request.POST.keys())
    try:
        username = request.POST['username']
        title = request.POST["title"]
        body = request.POST["body"]
    except (KeyError):
        # Redisplay the form.
        return render(request, 'ideas/idea_new.html', {
            'error_message': "Invalid form.",
        })
    
    newIdea = BusinessIdea(
        username = username,
        title = title,
        body = body,
        publish_date = datetime.now() 
    )
    newIdea.save()
    context = {
        "idea": newIdea
    }
    return HttpResponseRedirect(reverse("ideas:idea", args=(newIdea.id,)))
