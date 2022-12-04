from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
# from django.db.models import Q
import pytz
from datetime import datetime

# REST API 通信テスト用


class JPTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        # return Response(data={'status': dt_now}, status=status.HTTP_200_OK)
        jp = pytz.timezone('Asia/Tokyo')
        return JsonResponse(data={'status': datetime.now(tz=jp)}, status=status.HTTP_200_OK)


class USTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        us = pytz.timezone('US/Eastern')
        return JsonResponse(data={'status': datetime.now(tz=us)}, status=status.HTTP_200_OK)


class BRTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        br = pytz.timezone('Brazil/East')
        return JsonResponse(data={'status': datetime.now(tz=br)}, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html')
