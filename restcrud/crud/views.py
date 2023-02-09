from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
from .serializers import MovieListSerializer

@api_view(['GET','POST'])
def movie_list_create(request):

    if request.method =='GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies,many=True)

        return Response(data = serializer.data)

    if request.method == 'POST':

        serializer = MovieListSerializer(data=request.data)
        #유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
    
from django.shortcuts import render,get_object_or_404
@api_view(['GET','PATCH','DELETE'])
def movie_detail_update_delete(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PATCH' :
        serializer = MovieListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method =='DELETE':
        movie.delete()
        data={
            'movie':movie_pk
        }
        return Response(data)
