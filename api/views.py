from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import GroupSerializer, TeacherSerializer, StudentSerializer
from groups.models import Group, Teacher, Student


class GroupListView(ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.get_queryset()


class TeacherListView(ModelViewSet):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.get_queryset()


class StudentListView(ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.get_queryset()
