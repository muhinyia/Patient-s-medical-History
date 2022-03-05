from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Feedback
from patient.models import Patient
from patient.counties import Counties, Genders
from accounts.models import HealthOfficer
from django.contrib.auth.models import User


@login_required
def add_feedback(request):

    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        record_id = request.POST['record']
        officer = request.POST['officer']
        this_user = get_object_or_404(User, username=officer)

        #print("THIS OFFICER IS: {}".format(officer))
        this_officer = get_object_or_404(HealthOfficer, user=this_user)

        #print("THIS HEALTH OFFICER is: {}".format(this_officer))
        this_record = get_object_or_404(Patient, id=record_id)

        this_feedback = Feedback.objects.create(
            email=email, record=this_record, issue=message, reporting_officer=this_officer)

        this_feedback.save()

        record = get_object_or_404(Patient, pk=record_id)

        genders = Genders
        counties = Counties
        context = {'record': record, 'genders': genders, 'counties': counties}

        return redirect('patient:get_record')

        # return render(request, 'patient/patient_records.html', {'patients': patients, 'details': details, 'counties': counties, 'genders': genders})
