from dataclasses import field
from pydoc import describe
from rest_framework import serializers

from .models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','description','city','address')
        read_only_fields = ('id',)

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.IntegerField()
    company = serializers.IntegerField(source = 'company.id')

    def create(self, validated_data):
        n_company = validated_data.get('company')
        n_id = n_company.get('id')
        mcompany = Company.objects.get(id=n_id)
        vacancy = Vacancy.objects.create(name = validated_data.get('name'),description = validated_data.get('description'),salary=validated_data.get('salary'),company=(mcompany))
        return vacancy
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.salary = validated_data.get('salary')
        n_company = validated_data.get('company')
        n_id = n_company.get('id')
        mcompany = Company.objects.get(id=n_id)
        instance.company = mcompany
        instance.save()
        return instance

