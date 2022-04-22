import imp
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.request import HttpRequest
from django.http.response import HttpResponse,JsonResponse
from ..serializers import CompanySerializer, VacancySerializer

from ..models import Company, Vacancy

@api_view(['GET','POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serilizer = CompanySerializer(companies,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data,safe=False)
    elif request.method == 'POST':
        serilizer = CompanySerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        return Response(serilizer.errors)

@api_view(['GET','PUT',"DELETE"])
def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'message' : str(e)},status=400)
    
    if request.method == 'GET':
        serilizer = CompanySerializer(company)
        return Response(serilizer.data)
    elif request.method == 'PUT':
        serilizer = CompanySerializer(instance=company, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return Response({'message': 'this product is deleted'}, status=204)

@api_view(['GET','POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacansies = Vacancy.objects.all()
        serializer = VacancySerializer(vacansies,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

api_view(['GET','PUT','DELETE'])
def vacancy_detail(request,vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message' : str(e)},status=400)
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'message': 'this vacancy is deleted'}, status=204)