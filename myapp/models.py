from django.db import models

class WorkoutSession(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Workout Session on {self.date}"

class WorkoutDetail(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, related_name='workout_details', on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    sets = models.CharField(max_length=100)
    reps = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.exercise_name} - {self.sets} sets of {self.reps} reps at {self.weight}kg"
