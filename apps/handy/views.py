from django.shortcuts import render
from django.shortcuts import render, redirect
import bcrypt
import re
from apps.handy.models import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
        return render(request, 'handy/index.html')

    request.session['counter'] += 1
    if request.session['counter'] ==1:
        request.session.flush()
    return render(request, 'handy/index.html')

def register(request):
    errors = []
    request.session['error_msg'] = errors

    if len(request.POST['first_name']) < 1:
        errors.append("Your First Name is too short")
    if len(request.POST['last_name']) < 1:
        errors.append("Your Last Name is too short")
    if len(request.POST['email']) < 1:
        errors.append("Your Email is too short")
    if not EMAIL_REGEX.match(request.POST['email']):
        errors.append("Invalid Email")
    if len(request.POST['password']) < 8:
        errors.append("Your Password is too short")
    if request.POST['confirm'] != request.POST['password']:
        errors.append("Your Passwords do not match")

    if len(errors) > 0:
        print('EEEEERRRRROOOOORRRRRRS', errors)
        return redirect('/')

    else:
        request.session['logged_in'] = True

        firstname = request.POST['first_name']  #created variables to feed into table 
        lastname = request.POST['last_name']    #table input starts right below
        email = request.POST['email']
        password = request.POST['password']
        hashbrown = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        User.objects.create(first_name = firstname, last_name = lastname, email = email, password = hashbrown)

        c = User.objects.get(first_name = request.POST['first_name'])
        request.session['first_name'] = c.first_name
        id = c.id
        request.session['user_id'] = id
        print(id)

    return redirect('/dashboard')

def login(request):
    errors = []

    if len(request.POST['login_email']) < 1:
        errors.append("Invalid Credentials")
    if len(request.POST['login_password']) < 1:
        errors.append("Invalid Credentials")
    if len(errors) > 0:
        print('EEEEERRRRROOOOORRRRRRS', errors)
        request.session['login_error'] = errors
        return redirect('/')

    a = User.objects.filter(email = request.POST['login_email'])
    a = a[0]
    if a and bcrypt.checkpw(request.POST['login_password'].encode(), a.password.encode()):
        print(a.first_name)
        request.session['first_name'] = a.first_name
        request.session['user_id'] = a.id
        print(request.session['user_id'])
        return redirect('/dashboard')
    else:
        errors.append("Invalid Credential")
        request.session['login_error'] = errors
        return redirect('/')

def dashboard(request):
    this_user = User.objects.get(id=request.session['user_id'])

    user_jobs = this_user.saved_jobs.all()

    context = {
        'user':User.objects.all(),
        'job': Jobs.objects.all(),
        'my': user_jobs
    }
    print("TTTTTHHHHIIIISSSSS CONTEXT", context)
    return render(request, 'handy/dashboard.html', context)

def logoff(request):
    request.session.flush()
    return redirect('/')

def addpage(request):
    return render(request, 'handy/addjob.html')

def add(request):
    print("**********", request.session['user_id'])
    errors = []
    request.session['error_job'] = errors

    if len(request.POST['titles']) < 4:
        errors.append("Your Title is too short")
    if len(request.POST['description']) < 11:
        errors.append("Your Description is too short")
    if len(request.POST['location']) < 1:
        errors.append("Your Location must be filled out")
    if len(errors) > 0:
        print('EEEEERRRRROOOOORRRRRRS', errors)
        return redirect('/addpage')

    category = request.POST['category']
    titles = request.POST['titles']
    description = request.POST['description']
    location = request.POST['location']
    user_ids = request.session['user_id']
    print("THIS IS CATEGORY", category)
    Jobs.objects.create(
        category = category,
        title = titles,
        description = description,
        location = location,
        user_id = user_ids
    )
    return redirect('/dashboard')

def delete(request, id):
    d = Jobs.objects.get(id = id)
    d.delete()

    return redirect('/dashboard')

def view(request, id):
    b = User.objects.all()
    jobs = Jobs.objects.get(id = id)
    context = {
        "job" : jobs
    }
    print("User Name"*10, jobs.user_id)
    return render(request, 'handy/view.html', context)

def editpage(request, id):
    b = User.objects.all()
    jobs = Jobs.objects.get(id = id)
    context = {
        "job" : jobs
    }
    print("User Name"*10, jobs.user_id)
    return render(request, 'handy/edit.html', context)

def addmy(request, id):
    print("HEY WE MADE IT HERE THOUGH")
    # category_ = request.POST.get('category')
    # titles = request.POST.get('title')
    # description = request.POST.get('description')
    # location = request.POST.get('location')
    # user_ids = request.session['user_id']
    # job_id = request.POST.get('jobs_id')
    # created = request.POST.get('created_at')
    # updated = request.POST.get('updated_at')

    # print(category_, titles, description, location, user_ids, job_id, created, updated, "+++++++++++++++++++++++++++++")

    # MyJobs.objects.create(
    #     category = category_,
    #     title = titles,
    #     description = description,
    #     location = location,
    #     user_id = user_ids,
    #     created_at = created,
    #     updated_at = updated,
    #     jobs_id = job_id
    # )

    # d = Jobs.objects.get(id = id)
    # d.delete()
    this_user = User.objects.get(id=request.session['user_id'])
    this_job = Jobs.objects.get(id=id)
    this_job.saved_by.add(this_user)

    this_job.taken = 1
    this_job.save()

    return redirect('/dashboard')

def giveup(request, id):
    this_job = Jobs.objects.get(id=id)
    this_job.taken = 0
    this_job.save()

    return redirect('/dashboard')


def update(request):
    x = Jobs.objects.get(id = request.POST['id'])
    x.title = request.POST['edit_title']
    x.description = request.POST['edit_description']
    x.location = request.POST['edit_location']
    x.save()

    return redirect('/dashboard')