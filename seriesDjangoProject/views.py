from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import SearchForm
import services
"""This class defines the controllers for the application
each fonction is supposed to process a page and send it to thhe url mapper"""

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/searchResult/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})

def searchResult(request):
    service = services.Services()
    template = loader.get_template('searchResult.html')
    response=service.search_series_names(request.POST['search'])
    context={'response' : response}
    return HttpResponse(template.render(request=request, context=context))