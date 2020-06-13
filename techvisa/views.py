from django.shortcuts import render
from django.http import JsonResponse
from .models import Company
from datetime import datetime
import requests


def index(request):
    company_list = Company.objects.all()
    data = {
        "company_list": company_list
    }
    return render(request,'index.html', data)


def company(request):

    company_list = Company.objects.all()

    if request.method == 'POST':
        company_file = request.FILES['company-list']
        for chunk in company_file.chunks():
            for line in chunk.splitlines(True):
                company_line = line.decode('UTF-8')
                values = company_line.split(';')

                certification_date = datetime.strptime(values[2], '%d-%m-%Y')
                expiration_date = datetime.strptime(values[3], '%d-%m-%Y')
                company_values = {
                    'tax_number': values[0],
                    'name': values[1],
                    'certification_date': certification_date,
                    'expiration_date': expiration_date,
                }
                new_company = True
                for company in company_list:
                    if company.tax_number == company_values['tax_number']:
                        new_company = False
                        break

                if new_company:
                    Company(**company_values).save()
                
                
    company_list = Company.objects.all()
    data = {"company_list": company_list}

    return render(request,'company.html', data)


def job(request):
    job_url =request.POST['i-job-link']
    return render(request,'index.html', {"company_list":[]})