from rest_framework import generics, viewsets
from courses.models import Subject, Course
from courses.api.serializers import SubjectSerializer, CourseSerializer, CourseWithContentsSerializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from courses.api.permissions import IsEnrolled


class SubjectListView(generics.ListAPIView):
    """Retrieves a list of subject."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Retrieves a subject by pk."""

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Retrieves list of courses or a course with contents
     and allow enrollment."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
