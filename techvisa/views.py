from django.shortcuts import render
from django.http import JsonResponse
from .models import Company
from datetime import datetime
from requests import get
from bs4 import BeautifulSoup


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
                
    data = {'company_list': company_list}

    return render(request, 'company.html', data)


def job(request):
    job_url = request.POST['i-job-link']
    
    if job_url[-3:] == 'p=1':
        job_url = job_url[:-1]
    
    job_list = []
    for p in range(1, 4):
        response = get(f'{job_url}{p}')
        print(f'{job_url}{p}')
        if response.status_code == 200:

            page = BeautifulSoup(response.text, 'html.parser')
            div_list = page.findAll('div', attrs={'class':'card__job-c'})

            company_list = Company.objects.all()

            for item in div_list:
                job_name = item.find('a', attrs={'class': 'card__job-link'})
                local = item.find('div', attrs={'class': 'card__job-location'})
                company_name = item.find('div', attrs={'class': 'card__job-empname-label'})
                href = job_name.get('href')
                link = f'http://neuvoo.pt{href}'
                line = {
                    'link': link,
                    'job_name': job_name.text.strip(),
                    'local': local.text.strip(),
                    'company_name': company_name.text.strip(),
                }
                for company in company_list:
                    if line['company_name'] in company.name:
                        job_list.append(line)

        else:
            break

    data = {
        'job_list': job_list,
        'i_job_link': f'{job_url}{1}',
    }

    return render(request, 'index.html', data)
    