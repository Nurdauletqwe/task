from django.shortcuts import render
from rest_framework.response import Response
from .models import Rubric
from .serializer import RubricSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


@permission_classes((IsAuthenticated, ))
class APIRubricsViewSet(ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer

class APIReadonlyRubricinViewSet(ReadOnlyModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
    permission_classes = (IsAuthenticated, )