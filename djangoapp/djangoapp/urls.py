# ================================================== 
# Title: URLS
# Author: Mattithyahu 
# Created Date: 08/07/2023  
# ==================================================

# Imports
# ==================================================
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),
]
