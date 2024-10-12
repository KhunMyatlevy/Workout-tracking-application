from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkoutSessionForm, WorkoutDetailForm
from .models import WorkoutSession

# Step 1: Create Workout Session
def create_workout_session(request):
    if request.method == 'POST':
        session_form = WorkoutSessionForm(request.POST)
        if session_form.is_valid():
            workout_session = session_form.save()  # Save the workout session
            # Redirect to the view where user can add workout details to the session
            return redirect('add_workout_details', session_id=workout_session.id)
    else:
        session_form = WorkoutSessionForm()
    
    return render(request, 'create_workout_session.html', {
        'session_form': session_form,
    })

# Step 2: Add Workout Details to an existing Workout Session
def add_workout_details(request, session_id):
    workout_session = get_object_or_404(WorkoutSession, pk=session_id)

    if request.method == 'POST':
        detail_form = WorkoutDetailForm(request.POST)
        if detail_form.is_valid():
            workout_detail = detail_form.save(commit=False)
            workout_detail.workout_session = workout_session  # Link the detail to the session
            workout_detail.save()
            return redirect('add_workout_details', session_id=workout_session.id)  # Stay on the same page to add more details
    else:
        detail_form = WorkoutDetailForm()

    return render(request, 'add_workout_details.html', {
        'workout_session': workout_session,
        'detail_form': detail_form,
    })


from django.shortcuts import render
from .models import WorkoutSession

def view_workout_sessions(request):
    # Get all workout sessions from the database
    workout_sessions = WorkoutSession.objects.all()
    
    # Pass the workout sessions to the template
    return render(request, 'view_workout_sessions.html', {'workout_sessions': workout_sessions})

from django.shortcuts import render, get_object_or_404
from .models import WorkoutSession, WorkoutDetail

def view_workout_details(request, session_id):
    # Get the workout session by ID or show a 404 if not found
    workout_session = get_object_or_404(WorkoutSession, id=session_id)

    # Get all workout details related to this session
    workout_details = WorkoutDetail.objects.filter(workout_session=workout_session)

    # Pass the session and details to the template
    return render(request, 'view_workout_details.html', {
        'workout_session': workout_session,
        'workout_details': workout_details
    })
