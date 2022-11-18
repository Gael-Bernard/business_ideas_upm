from django.contrib import admin

from .models import BusinessIdea, IdeaComment

# Register your models here.
admin.site.register(BusinessIdea)
admin.site.register(IdeaComment)