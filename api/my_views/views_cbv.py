from ast import Delete
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import Http404
from ..serializers import CompanySerializer, VacancySerializer
from ..models import Company, Vacancy
from rest_framework.permissions import IsAuthenticated

class CompanyListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        companies = Company.objects.all()
        serilizer = CompanySerializer(companies,many=True)
        #companies_json = [company.to_json() for company in companies]
        return Response(serilizer.data)
    def post(self,request):
        serilizer = CompanySerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)

class CompanyDetailAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
           return Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
           raise Http404
    
    def get(self,request,pk=None):
        company = self.get_object(pk)
        serilizer = CompanySerializer(company)
        return Response(serilizer.data)
    
    def put(self,request,pk=None):
        company = self.get_object(pk)
        serilizer = CompanySerializer(instance=company, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    
    def delete(self,request,pk=None):
        company = self.get_object(pk)
        company.delete()
        return Response({'message': 'this product is deleted'}, status=204)

class VacancyListAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        vacansies = Vacancy.objects.all()
        #vacancies_json = [vacancy.to_json() for vacancy in vacansies]
        serializer = VacancySerializer(vacansies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class VacancyDetailAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self,pk):
        try:
            return Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist as e:
            raise Http404

    def get(self,request,pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data) 
    
    def put(self,request,pk=None):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(instance=vacancy,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response({'message': 'this vacancy is deleted'}, status=204)

          


        
