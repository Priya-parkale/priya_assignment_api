from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

# Create your views here.
class OpenWeather(APIView):
    def get(self, request):
        data = request.data
        return Response(data)
    
    def post(self, request):
        # get data for example like this
        
        """
            {
                "month": 4,
                "day": 11,
                "year": 2020
            }
        """
        data = request.data
        # check day is prime or Not
        _day = data['day'] or 1
        
        is_prime = False
        if _day > 1:   
            for i in range(2, _day): 
                if (_day % i) == 0: 
                    return Response({"success": f"{_day} is a Not Prime number"})
                    break
            else: 
                return Response({"success": f"{_day} is a Prime number"})
        else: 
            return Response({"success": f"{_day} is a Not Prime number"})
        return Response(data)

