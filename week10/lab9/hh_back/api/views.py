from django.shortcuts import render

from django.http.response import JsonResponse
from api.models import Company, Vacancy


def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancy_json = [vacancy.full() for vacancy in vacancies]
        return JsonResponse(vacancy_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'ERROR': str(e)})
    return JsonResponse(vacancy.full())


def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')
    vacancy_json = [vacancy.full() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)


def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'ERROR': str(e)})
    return JsonResponse(company.full())


def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.full() for company in companies]
    return JsonResponse(companies_json, safe=False)


def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'ERROR': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.full() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
