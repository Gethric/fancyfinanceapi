from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrenciesListView.as_view(), name='currencies_list'),
    path('user-currencies/', views.UserCurrenciesListView.as_view(), name='user_currencies_list'),
    path('pitches/', views.PitchesListView.as_view(), name='pitches_list'),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
]