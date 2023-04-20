from django.urls import path
from core.erp.views.category.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.plan.views import *


app_name = 'erp'

urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    # plan
    path('plan/list/', PlanListView.as_view(), name='plan_list'),
    path('plan/add/', PlanCreateView.as_view(), name='plan_create'),
    path('plan/update/<int:pk>/', PlanUpdateView.as_view(), name='plan_update'),
    path('plan/delete/<int:pk>/', PlanDeleteView.as_view(), name='plan_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
   
]
