# ================================================== 
# Title: REST APIs (Datetime in Timezones)
# Author: Mattithyahu 
# Created Date: 08/07/2023  
# ==================================================

# Imports
# ==================================================
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
import pytz


# API View to Return Time in Europe/LDN
# ==================================================
class Return_Time_LDN(APIView):

    # POST Method
    def post(self, request):
        data = request.data
        keys = []
        values = []
        if len(data) > 0:
            for key in data:
                keys.append(key)
                values.append(data[key])

        # Getting Time as GMT / BST
        current_time = datetime.now(pytz.timezone('Europe/London')).strftime("%H:%M:%S")
        current_date = datetime.now(pytz.timezone('Europe/London')).strftime("%d/%m/%Y")

        # Response data
        data = {
            'time': current_time,
            'date': current_date,
        }

        # RESPONSE
        return Response(data, status=200)
    
    
# API View to Return Time in America/Los_Angeles
# ==================================================
class Return_Time_LA(APIView):

    # POST Method
    def post(self, request):
        data = request.data
        keys = []
        values = []
        if len(data) > 0:
            for key in data:
                keys.append(key)
                values.append(data[key])

        # Getting Time as PST / PDT
        current_time = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%H:%M:%S")
        current_date = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%d/%m/%Y")

        # Response data
        data = {
            'time': current_time,
            'date': current_date,
        }

        # RESPONSE
        return Response(data, status=200)