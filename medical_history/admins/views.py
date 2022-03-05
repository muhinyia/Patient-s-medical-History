from facilities.models import Facility
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404, render, redirect
from patient.models import Patient, PatientBio
from django.contrib import messages, auth
from accounts.models import HealthOfficer
from feedback.models import Feedback
# Create your views here.


def index(request):
    physicians = HealthOfficer.objects.all()
    patients = PatientBio.objects.all()
    records = Patient.objects.all()
    feedbacks = Feedback.objects.all()
    context = {'physicians': physicians, 'patients': patients,
               'records': records, 'feedbacks': feedbacks, }
    return render(request, 'admin/admins_dashboard.html', context)


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
            return redirect('admins:index')
        else:

            this_patient = PatientBio.objects.create(
                huduma_id=huduma_id, first_name=first_name, last_name=last_name, dob=dob, phone=phone, gender=gender, county=county)

            this_patient.save()
            messages.success(request, 'Patient added Successfully')

            return redirect('admins:index')


def add_doc(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        id_number = request.POST['id_number']
        reg_number = request.POST['reg']
        title = request.POST['title']
        email = request.POST['email']
        facility = request.POST['facility']
        pic = request.FILES['pic']

        # get the facility
        this_facility = get_object_or_404(Facility, name=facility)

        # check username
        if User.objects.filter(username=reg_number).exists():
            messages.error(
                request, "Registration Number Already in the System!")
            return redirect('admins:index')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, "Registration Number Already in the System!")
                return redirect('admins:index')
            else:
                # seems user is ready to be registered
                user = User.objects.create_user(
                    username=reg_number, password=id_number, email=email, first_name=first_name, last_name=last_name)
                user.save()

                # adding to HealthOfficer model:
                this_user = User.objects.get(username=reg_number)
                if this_user is not None:
                    this_doc = HealthOfficer.objects.create(
                        user=this_user, id_number=id_number, reg_number=reg_number, title=title, phone=phone, facility=this_facility, email=email, pic=pic)  # for now set is_hired to True but remember to change it later for admin control
                    this_doc.save()

                messages.success(
                    request, 'The Physician Was registered successfully')
                return redirect('admins:index')

    return redirect('admins:index')


def add_facility(request):
    if request.method == 'POST':
        facility_no = request.POST['facility_no']
        level = request.POST['level']
        name = request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        category = request.POST['category']
        phone = request.POST['phone']
        county = request.POST['county']

        this_facility = Facility.objects.create(
            facility_no=facility_no, name=name, facility_level=level, city=city, address=address, phone=phone, is_public=category, county=county)

        this_facility.save()
        messages.success(request, 'Facility added Successfully')

        return redirect('admins:index')


def get_patients(request):
    patients = PatientBio.objects.all()
    return render(request, 'admin/patients.html', {'patients': patients})


def get_docs(request):
    physicians = HealthOfficer.objects.all()
    return render(request, 'admin/officers.html', {'physicians': physicians})


def get_facilities(request):
    facilities = Facility.objects.all()
    return render(request, 'admin/facilities.html', {'facilities': facilities})


def get_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin/feedbacks.html', {'feedbacks': feedbacks})


def get_records(request):
    records = Patient.objects.all()
    return render(request, 'admin/records.html', {'records': records})
