from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from account.forms import *
from jobapp.permission import user_is_employee, user_is_employer
from interview_scheduler.models import InterviewSchedule

from django.urls import reverse_lazy
from django.shortcuts import render
from jobapp.models import Job

@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_employee
def applicant_interview_handler(request, id, job_id):

    job = Job.objects.filter(pk=job_id)
    interview_schedule = InterviewSchedule.objects.filter(job=job[0], applicant=request.user)[0]
    rejected = False
    if interview_schedule.current_status == 0:
        rejected = True
    elif request.method == "POST":

        slot_num = request.POST.get('interview_slot')
        print("slot num = ", slot_num)
        interview_schedule.round_status = 1
        print(interview_schedule.interview_slot1)
        print(interview_schedule.interview_slot2)
        print(interview_schedule.interview_slot3)
        if slot_num == '2':
            temp = interview_schedule.interview_slot1
            interview_schedule.interview_slot1 = interview_schedule.interview_slot2
            interview_schedule.interview_slot2 = temp
        elif slot_num == '3':
            temp = interview_schedule.interview_slot1
            interview_schedule.interview_slot1 = interview_schedule.interview_slot3
            interview_schedule.interview_slot3 = temp
        interview_schedule.save()
        print(interview_schedule.interview_slot1)
        print(interview_schedule.interview_slot2)
        print(interview_schedule.interview_slot3)
    context = {
        'interview_schedule': interview_schedule,
        'job_id':job_id,
        'rejected': rejected
    }
    return render(request, 'interview_scheduler/applicant-interview-handler.html', context)


from datetime import datetime


def get_datetime(s):
    return datetime(int(s[0:4]), int(s[5:7]), int(s[8:10]), int(s[11:13]), int(s[14:16]))

from .models import ROUNDS

@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_employer
def recruiter_interview_handler(request, id, job_id):
    job = Job.objects.filter(pk=job_id)
    previous_round = InterviewSchedule.objects.filter(job=job[0], recruiter=request.user)[0].round
    show = True
    if request.method == "POST":
        current_status = int(request.POST.get('current_status'))
        if current_status == 0:
            pass
        #     Reject the candidate
        elif current_status == 2:
            pass
        #     Make an offer
        num_rounds = int(request.POST.get('num_rounds'))
        round_status = request.POST.get('round_status')
        interviewer_email = request.POST.get('interviewer-email')

        interview_slot1 = get_datetime(request.POST.get('interview-slot-1'))
        interview_slot2 = get_datetime(request.POST.get('interview-slot-2'))
        interview_slot3 = get_datetime(request.POST.get('interview-slot-3'))
        round_link = request.POST.get('round_link')
        current_round = request.POST.get('current_round')
        interview_schedule = InterviewSchedule.objects.filter(job=job[0], recruiter=request.user)
        if interview_schedule is not None:
            interview_schedule = interview_schedule[0]
            interview_schedule.email_id_of_interviewer = interviewer_email
            interview_schedule.current_status = int(current_status)
            interview_schedule.num_rounds = int(num_rounds)
            interview_schedule.interview_slot1 = interview_slot1
            interview_schedule.interview_slot2 = interview_slot2
            interview_schedule.round_status = 0
            interview_schedule.interview_slot3 = interview_slot3
            interview_schedule.round_link = round_link
            interview_schedule.round = current_round
            interview_schedule.save()
            current_round = InterviewSchedule.objects.filter(job=job[0], recruiter=request.user)[0].round
            if current_round > previous_round:
                show = False
    context = {
        'interview_schedule': InterviewSchedule.objects.filter(job=job[0], recruiter=request.user)[0],
        'applicant_id': id,
        'job_id': job_id,
        'show':show
    }
    return render(request, 'interview_scheduler/recruiter-interview-handler.html', context)