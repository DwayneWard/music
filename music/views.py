from django.shortcuts import render
from django.views import View
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, GenericAPIView, RetrieveAPIView, \
    DestroyAPIView, get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from music.models import Track, Selection
from music.permissions import SelectionEditPermission
from music.serializers import StaredTrackSerializer, \
    SelectionDetailSerializer, SelectionSerializer


class TrackView(ListAPIView):
    queryset = Track.objects.all()
    serializer_class = StaredTrackSerializer
    permission_classes = [permissions.AllowAny, ]


class TrackRetrieveView(RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = StaredTrackSerializer
    permission_classes = [permissions.AllowAny, ]

class TracksView(View):
    queryset = Track.objects.all()
    serializer_class = StaredTrackSerializer
    permission_classes = [permissions.AllowAny, ]


def show_track(request, track_slug):
    track = get_object_or_404(Track, slug=track_slug)

    context = {
        'name': track.name,
        'author': track.author,
        'release_date': track.release_date,
        'genre': track.genre,
        'duration_in_seconds': track.duration_in_seconds,
        'album': track.album,
        'logo': track.logo,
        'stared_user': track.stared_user,
        'slug': track.slug
    }

    return Response(context)

class StaredTrackView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        bad_request_message = 'An error has occurred'

        track = get_object_or_404(Track, id=kwargs.get('pk'))
        if request.user not in track.stared_user.all():
            track.stared_user.add(request.user)
            return Response({'detail': 'User added to track'})
        return Response({'detail': bad_request_message})

    def delete(self, request, *args, **kwargs):
        bad_request_message = 'An error has occurred'
        track = get_object_or_404(Track, id=kwargs.get('pk'))
        if request.user in track.stared_user.all():
            track.stared_user.remove(request.user)
            return Response({'detail': 'User removed from track'})
        return Response({'detail': bad_request_message})

class StaredTracksView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        bad_request_message = 'An error has occurred'
        ids = request.query_params['id'].split(',')
        tracks = []
        for i in ids:
            tracks.append(get_object_or_404(Track, id=int(i)))
        for track in tracks:
            if request.user not in track.stared_user.all():
                track.stared_user.add(request.user)
            else:
                return Response({'detail': bad_request_message})
        return Response({'detail': 'User added to track'})

    def delete(self, request, *args, **kwargs):
        bad_request_message = 'An error has occurred'
        ids = request.query_params['id'].split ( ',')
        tracks = []
        for i in ids:
            tracks.append(get_object_or_404(Track, id=int(i)))
        for track in tracks:
            if request.user not in track.stared_user.all ():
                track.stared_user.remove(request.user)
            else:
                return Response({'detail': bad_request_message})
        return Response({'detail': 'User added to track'})


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionRetrieveView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, ]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]


class SelectionDestroyView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionEditPermission]
