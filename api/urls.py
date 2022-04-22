from django.urls import path
from api.views import company_list
from rest_framework_jwt.views import obtain_jwt_token  
#from views import company_list
from api.views import vacancy_list,vacancies_by_company
from api.views import company_detail,vacancy_detail,vacancy_list_sorted
from .my_views.views_cbv import CompanyDetailAPIView, CompanyListAPIView, VacancyDetailAPIView, VacancyListAPIView

urlpatterns = [
    path('login/',obtain_jwt_token),
    path('companies/',CompanyListAPIView.as_view()),
    path('companies/<int:pk>/',CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/',vacancies_by_company),
    path('vacancies/',VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/',VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/',vacancy_list_sorted)
]
