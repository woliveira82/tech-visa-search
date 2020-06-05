from django.shortcuts import render
from .models import Company


def index(request):
    company_list = Company.objects.all()
    data = {
        "company_list": company_list
    }
    return render(request,'index.html', data)
