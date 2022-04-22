import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
# Create your views here.


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serilizer = CompanySerializer(companies,many=True)
        #companies_json = [company.to_json() for company in companies]
        return JsonResponse(serilizer.data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        # try:
        #     company = Company.objects.create(name=data['name'],description = data['description'],city=data['city'],address=data['address'])
        # except Exception as e:
        #     return JsonResponse({'message': str(e)})

        # serilizer = CompanySerializer(company)
        # return JsonResponse(serilizer.data)
        serilizer = CompanySerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        return JsonResponse(serilizer.errors)

@csrf_exempt
def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message' : str(e)},status=400)
    
    if request.method == 'GET':
        serilizer = CompanySerializer(company)
        return JsonResponse(serilizer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        # company.name = data['name']
        # company.description = data['description']
        # company.city = data['city']
        # company.address = data['address']
        # company.save()
        serilizer = CompanySerializer(instance=company, data=data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        return JsonResponse(serilizer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'this product is deleted'}, status=204)

def vacancies_by_company(request,company_id):
    vacancies = Vacancy.objects.filter(company = company_id).all()
    if vacancies:
         vacancies_json = [vacancy.to_json() for vacancy in vacancies]
         return JsonResponse(vacancies_json,safe=False)
    else:
        return JsonResponse({'message' : 'Vacancies in this company does not exists'},status=400)

@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacansies = Vacancy.objects.all()
        #vacancies_json = [vacancy.to_json() for vacancy in vacansies]
        serializer = VacancySerializer(vacansies,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        #try:
            #body_company = Company.objects.get(id=data['company'])
            #vacancy = Vacancy.objects.create(name=data['name'],description = data['description'],salary=data['salary'],company=body_company)
        #except Exception as e:
           # return JsonResponse({'message': str(e)})
        
        #return JsonResponse(vacancy.to_json(),safe=False)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def vacancy_detail(request,vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message' : str(e)},status=400)
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        # vacancy.name = data['name']
        # vacancy.description = data['description']
        # vacancy.salary = data['salary']
        # body_company = Company.objects.get(id=data['company_id'])
        # vacancy.company = body_company
        # vacancy.save()
        serializer = VacancySerializer(instance=vacancy,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'this vacancy is deleted'}, status=204)

def vacancy_list_sorted(request):
    vacansies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacansies]
    return JsonResponse(vacancies_json,safe=False)
