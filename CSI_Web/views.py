import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from CSI_Web.models import CarouselInfo, InventionInfo
from CSI_Web.models import ProblemInfo

def index(request):
    carousel_info = CarouselInfo.objects.all()
    return render(request, 'index.html', {'carousel_info': carousel_info})


@csrf_exempt
def submit_problem(request):
    try:
        problem_category = request.POST.get('problemCategory')
        problem_description = request.POST.get('problemDescription')
        name = request.POST.get('name')
        contact_number = request.POST.get('contactNumber')
        contact_address = request.POST.get('contactAddress')
        email_ID = request.POST.get('emailID')
        problem_info = ProblemInfo(problem_category=problem_category,
                                   problem_description=problem_description,
                                   name=name,
                                   contact_number=contact_number,
                                   contact_address=contact_address,
                                   email_id=email_ID)
        problem_info.save()
        return HttpResponse(json.dumps({"success": "Your problem is with us. "
                                                   "A member from our community will contact you shortly"}), content_type="application/json")

    except():
        return HttpResponse(json.dumps({"error": "Something went wrong. Try again later."}), content_type="application/json")


@csrf_exempt
def submit_invention(request):
    try:
        invention = request.POST.get('invention')
        problem_description = request.POST.get('problemDescription')
        team = request.POST.get('team')
        contact_number = request.POST.get('contactNumber')
        email_ID = request.POST.get('emailID')
        # return HttpResponse(json.dumps({"error": "Something went wrong. Try again later."}), content_type="application/json")
        invention_info = InventionInfo(invention=invention,
                                       abstract=problem_description,
                                       team_details=team,
                                       contact_number=contact_number,
                                       email_id=email_ID)
        invention_info.save()
        return HttpResponse(json.dumps({"success": "Your invention is with us. "
                                                   "A member from our community will contact you shortly"}),
                            content_type="application/json")
    except():
        return HttpResponse(json.dumps({"error": "Something went wrong. Try again later."}), content_type="application/json")
