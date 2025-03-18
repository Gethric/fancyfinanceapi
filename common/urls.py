from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrenciesListView.as_view(), name='currencies-list'),
    path('usercurrencies/', views.UserCurrenciesListView.as_view(), name='usercurrencies-list'),
    path('pitches/', views.PitchesListView.as_view(), name='pitches-list'),
    path('categories/', views.CategoriesListView.as_view(), name='categories-list'),
]