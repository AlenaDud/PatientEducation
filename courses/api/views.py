from rest_framework import generics
from courses.models import Subject
from courses.api.serializers import SubjectSerializer


class SubjectListView(generics.ListAPIView):
    """Retrieves a list of subject."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """Retrieves a subject by pk."""
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


