from django.urls import path

from music import views

urlpatterns = [
    path('track/all/', views.TrackView.as_view()),
    path('track/<int:pk>/', views.TrackRetrieveView.as_view()),
    path('track/<int:pk>/favorite/', views.StaredTrackView.as_view()),
]
