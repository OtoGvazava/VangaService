from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GamesSerializer
from .models import Games


@api_view(['GET'])
def gamesList(request):
    page = request.GET.get('page', 1)
    games = Games.objects.all()
    pages = Paginator(games, 3)
    if int(page) > pages.num_pages:
        return Response([])
    page = pages.page(page)
    serializer = GamesSerializer(page, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createGame(request):
    serializer = GamesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)