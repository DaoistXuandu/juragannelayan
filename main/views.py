
# Create your views here.
from django.shortcuts import render, redirect
from main.forms import NelayanEntryForm
from main.models import NelayanEntry 
from django.http import HttpResponse
from django.core import serializers

def show_json_by_id(request, id):
    data = NelayanEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = NelayanEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = NelayanEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = NelayanEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def create_item_entry(request):
    form = NelayanEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form }
    return render(request, "create_item_entry.html", context)

def show_main(request):
    item_entry = NelayanEntry.objects.all()

    context = {
        'app_name': 'Juragan Nelayan',
        'name': 'Raihan Akbar',
        'class': 'PBP E',
        'item_entry' : item_entry
    }

    return render(request, "main.html", context)


