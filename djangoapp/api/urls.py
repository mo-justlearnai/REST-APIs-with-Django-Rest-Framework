# ================================================== 
# Title: URLS
# Author: Mattithyahu 
# Created Date: 08/07/2023  
# ==================================================

# Imports
# ==================================================
from django.urls import path
import api.views as views

urlpatterns = [
    path('gettime/gb/', views.Return_Time_LDN.as_view(), name = 'api_time_gb'),
    path('gettime/la/', views.Return_Time_LA.as_view(), name = 'api_time_la'),
]
