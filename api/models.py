from tabnanny import verbose
from django.db import models

# Create your models here.

class Company(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=40,default='Ebay')
  description = models.TextField()
  city = models.CharField(max_length=40,default='Amsterdam') 
  address = models.CharField(max_length=40,default='Switzerland')
 
  class Meta:
      verbose_name = 'Company'
      verbose_name_plural = 'Companies'

  def to_json(self):
       return {
         'id': self.id,
         'name': self.name,
         'city': self.city,
         'description': self.description,
         'address': self.address
       }

class Vacancy(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=40,default='Ebay')
  description = models.TextField()
  salary = models.IntegerField(max_length=5) 
  company = models.ForeignKey('Company',on_delete=models.CASCADE,related_name='company')
 
  class Meta:
      verbose_name = 'Vacancy'
      verbose_name_plural = 'Vacancies'
      
  def to_json(self):
       return {
         'id': self.id,
         'name': self.name,
         'description': self.description,
         'salary': self.salary,
         'company': self.company.id 
       }

