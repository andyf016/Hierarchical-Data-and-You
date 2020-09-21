from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from hierarchyapp.models import File

class Index(TemplateView):

    def get(self, request):
        all_files = File.objects.all()
        return render(request, 'index.html', {'nodes': all_files})


