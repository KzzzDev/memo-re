from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from shop.models import Book
# from .serializers import BookSerializer


# class NoteViewSet(viewsets.ModelViewSet):
#     """NoteオブジェクトのCRUDをおこなうAPI"""

#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
