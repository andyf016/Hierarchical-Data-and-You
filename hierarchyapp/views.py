from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import TemplateView
from hierarchyapp.models import File
from hierarchyapp.forms import NewItemForm

class Index(TemplateView):

    def get(self, request):
        all_files = File.objects.all()
        return render(request, 'index.html', {'nodes': all_files})

class ItemFormView(TemplateView):

    def get(self, request):
        form = NewItemForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = NewItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = File.objects.create(
                name = data.get('name'),
                parent = data.get('parent')
            )
        return HttpResponseRedirect(reverse('home'))

