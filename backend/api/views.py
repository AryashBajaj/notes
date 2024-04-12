from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from .models import Note
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view

# Create your views here.

class CreateuserView(generics.ListCreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class NoteCreateView(generics.ListCreateAPIView) :
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid() :
            serializer.save(author = self.request.user)
        else :
            print(serializer.errors)

class NoteDeleteView(generics.DestroyAPIView) :
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
    
    
    

