from django.shortcuts import render

from CSI_Web.models import CarouselInfo


def index(request):
    carousel_info = CarouselInfo.objects.all()
    return render(request, 'index.html', {'carousel_info': carousel_info})