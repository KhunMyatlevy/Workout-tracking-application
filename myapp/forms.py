from django import forms
from .models import WorkoutSession, WorkoutDetail

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['date']  # Include only the fields you want to appear in the form

class WorkoutDetailForm(forms.ModelForm):
    class Meta:
        model = WorkoutDetail
        fields = ['workout_session', 'exercise_name', 'sets', 'reps', 'weight']  # Include all relevant fields
