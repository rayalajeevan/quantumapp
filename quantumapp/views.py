from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import SurveySerializer
import json
# Create your views here.


class PostSurvey(APIView):
    def post(self, request, *args, **kwrgs):
        try:
            try:
                data = json.loads(self.request.body)
            except Exception as exc:
                return Response({"status": "Failed", "description": "Invalid Json Format"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                ser_obj = SurveySerializer(data=data)
                if ser_obj.is_valid():
                    ser_obj.save()
                    return Response({"status": "Succses"}, status=status.HTTP_200_OK)
                return Response({"status": "Failed", "data": ser_obj.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({"status": str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def render_home_page(request):
    return render(request, "index.html")
