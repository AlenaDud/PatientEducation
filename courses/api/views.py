from rest_framework import generics
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class SubjectListView(generics.ListAPIView):
    """Retrieves a list of subject."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Retrieves a subject by pk."""

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    """Enrolls a patient in the current course."""

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
