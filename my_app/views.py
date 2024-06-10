from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, TaskForm
from . models import Task

# Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


def viewHome(request):
    """
    This function display base page of my_app.
    """
    return render(request, 'index.html')


def register(request):
    """
    This function creates user info from the registration form

        if 'POST'(info) is true and valid:
        it save and redirect to LOGIN page

        if not valid:
        redirect to REGISTER page
    """

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    context = {'registerform': form}

    return render(request, 'register.html', context=context)


def login(request):
    """
    This function takes "POST"(info) from register(request) and if it is valid,
    USER is allow to LOGIN

        if 'POST'(info) is valid:
        it authenticates username + password and redirect to DASHBOARD

        if not valid:
        redirect to LOGIN page
    """

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'loginform': form}

    return render(request, 'login.html', context=context)


def user_logout(request):
    """
    This function LOGOUT the user using authentication request

    Returns To the index page of my_app
    """

    auth.logout(request)

    return redirect("index")


def dashboard(request):
    """
    This function display tasks and the create task form.

        if "POST" request is valid:
        create task, save and return to DASHBOARD

        if is not valid:
        redirect to DASHBOARD page.
    """

    form = TaskForm()

    tasks = Task.objects.all()

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('dashboard')

        return redirect('/')

    context = {'tasks': tasks, 'Taskform': form}

    return render(request, 'dashboard.html', context)


def updateTasks(request, pk):
    """
    This function update tasks using primary key to get tasks

        if "POST" request is valid:
        update task, save and returns to DASHBOARD

        if is not valid:
        returns to delete tasks page.
    """

    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=tasks)

        if form.is_valid():

            form.save()

        return redirect('dashboard')

    contxt = {'TaskForm': form}

    return render(request, 'update_tasks.html', contxt)


def deleteTasks(request, pk):
    """
    This function delete tasks objects using primary key to get tasks

        if "POST" request is valid:
        delete task and returns to DASHBOARD

        if is not valid:
        returns to delete tasks page.
    """

    tasks = Task.objects.get(id=pk)

    if request.method == 'POST':

        tasks.delete()

        return redirect('dashboard')
    contxt = {'task': tasks}

    return render(request, 'delete_tasks.html', contxt)
