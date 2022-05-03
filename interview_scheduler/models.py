from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
from jobapp.models import Job

ROUNDS = (
    ('1', 'Round 1'),
    ('2', 'Round 2'),
    ('3', 'Round 3'),
    ('4', 'Round 4'),
    ('5', 'Round 5'),
)

class InterviewSchedule(models.Model):
    job = models.ForeignKey(Job, related_name='Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='Employee', on_delete=models.CASCADE)
    recruiter = models.ForeignKey(User, related_name='Employer', on_delete=models.CASCADE)
    # Number of rounds
    num_rounds = models.IntegerField(default=5)
    # Current Round
    round = models.IntegerField(choices=ROUNDS, default=1)
    # If current_status = 0, then candidate is rejected, 1 means still ongoing, 2 means selected
    current_status = models.IntegerField(default=-1)
    # Interviewer who will take the interview to notify them.
    email_id_of_interviewer = models.EmailField(null=True, blank=True)
    # value is 0, recruiter added but candidate have not selected.
    # value is 1, candidate have confirmed.
    round_status = models.IntegerField(default=0)
    interview_slot1 = models.DateTimeField(null=True, auto_now=False)
    interview_slot2 = models.DateTimeField(null=True, auto_now=False)
    interview_slot3 = models.DateTimeField(null=True, auto_now=False)
    # Link of platform on which the round will take place.
    round_link = models.URLField(null=True)

    def __str__(self):
        return str(self.job)
