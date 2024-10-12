from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_workout_session, name='create_workout_session'),
    path('workout-session/<int:session_id>/add-details/', views.add_workout_details, name='add_workout_details'),
    path('workout-sessions/', views.view_workout_sessions, name='view_workout_sessions'),
    path('workout-sessions/<int:session_id>/', views.view_workout_details, name='view_workout_details'),



]
