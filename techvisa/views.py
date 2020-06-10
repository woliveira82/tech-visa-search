from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from .models import Company


def index(request):
    company_list = Company.objects.all()
    data = {
        "company_list": company_list
    }
    return render(request,'index.html', data)


@require_http_methods(["POST"])
def post_company(request):
    company_list = request.FILES['file'].read()
    data = csv.DictReader(company_list)
    print(type(data))
    print(data)

    return render(request,'index.html', data)
