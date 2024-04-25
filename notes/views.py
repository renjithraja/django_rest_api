from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET'])
def get_all_notes(request):
    notes = Notes.objects.all()
    serializer = NotesSerializer(notes, many=True)
    return Response(serializer.data)

# Create view
@csrf_exempt
@api_view(['POST'])
def create_note(request):
    serializer = NotesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve view
@csrf_exempt
@api_view(['GET'])
def get_note_detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = NotesSerializer(note)
    return Response(serializer.data)

# Update view
@csrf_exempt
@api_view(['PUT'])
def update_note(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = NotesSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete view
@csrf_exempt
@api_view(['DELETE'])
def delete_note(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
@api_view(['GET'])
def search_notes(request):
    query = request.GET.get('query')
    if query:
        searched_notes = Notes.objects.filter(name__icontains=query)
    else:
        searched_notes = Notes.objects.all()
    serializer = NotesSerializer(searched_notes, many=True)
    return Response(serializer.data)
