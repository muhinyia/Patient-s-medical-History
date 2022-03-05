from django.contrib import auth, messages
from facilities.models import Facility
from accounts.models import HealthOfficer
from .models import PatientBio, Patient
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Patient, PatientBio
from django.contrib.auth.decorators import login_required
from .counties import Counties, Genders
from django.contrib.auth.models import User


@login_required
def get_patient(request):
    if request.method == 'POST':
        huduma_id = request.POST['huduma_id']

        patients = PatientBio.objects.filter(huduma_id=huduma_id)[:1]

        details = Patient.objects.filter(patient=huduma_id).order_by('-date')

        genders = Genders
        counties = Counties

        return render(request, 'patient/patient_records.html', {'patients': patients, 'details': details, 'counties': counties, 'genders': genders})


@login_required
def get_patient_back(request, id):
    patients = PatientBio.objects.order_by(
        'huduma_id').filter(huduma_id=id)[:1]
    details = Patient.objects.filter(patient=id).order_by('-date')
    genders = Genders
    counties = Counties
    huduma_id = id
    return render(request, 'patient/patient_records.html', {'patients': patients, 'details': details, 'counties': counties, 'genders': genders, 'huduma_id': huduma_id})


@login_required
def get_record(request, record_id):
    record = get_object_or_404(Patient, pk=record_id)

    genders = Genders
    counties = Counties
    context = {
        'record': record, 'genders': genders, 'counties': counties
    }

    return render(request, 'patient/more_details.html', context)


@login_required
def enter_record(request):
    if request.method == 'POST':
        huduma_id = request.POST['huduma_id']
        officer = request.POST['officer']
        symptoms = request.POST['symptoms']
        lab_works = request.POST['lab_works']
        diagnosis = request.POST['diagnosis']
        treatment = request.POST['treatment']
        comment = request.POST['comment']
        docs = request.FILES['documents']
        x_ray = request.FILES['x_ray']

        this_user = get_object_or_404(User, username=officer)
        this_officer = get_object_or_404(HealthOfficer, user=this_user)
        this_patient = get_object_or_404(PatientBio, huduma_id=huduma_id)
        this_faciilty = this_officer.facility

        this_record = Patient.objects.create(patient=this_patient, facility=this_faciilty, health_officer=this_officer, presenting_symptoms=symptoms,
                                             lab_works=lab_works, diagnosis_made=diagnosis, treatment_offered=treatment, comment=comment, x_ray=x_ray, docs=docs)

        this_record.save()
        #messages.success(request, 'Record entered Successfully')

        return render(request, 'accounts/success.html')


def add_patient(request):
    if request.method == 'POST':
        huduma_id = request.POST['huduma_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        phone = request.POST['phone']
        county = request.POST['county']

        if PatientBio.objects.filter(huduma_id=huduma_id).exists():
            messages.error(
                request, "This Patient is Already in the System!")
            return redirect('accounts:dashboard')
        else:

            this_patient = PatientBio.objects.create(
                huduma_id=huduma_id, first_name=first_name, last_name=last_name, dob=dob, phone=phone, gender=gender, county=county)

            this_patient.save()
            messages.success(request, 'Patient added Successfully')

            return redirect('accounts:dashboard')
