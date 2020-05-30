from django.shortcuts import render

# Create your views here.

def traveler_main(request):
    return render(request, 'traveler_main.html')

def traveler_list(request):
    return render(request, 'traveler_list.html')

def traveler_detail(request):
    return render(request, 'traveler_detail.html')

def traveler_search(request):
    return render(request, 'traveler_search.html')