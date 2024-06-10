# Building a Django CRUD (Create, Retrieve, Update and Delete) Project 

Django is a powerful Python web framework that simplifies web development by providing a clean and pragmatic design. 



- Python and Django: Ensure you have Python installed on your system. You can install Django using pip:
pip install django
- Database: Decide on the database you want to use. 
- By default, Django uses SQLite, but you can configure it to use other databases like PostgreSQL, MySQL, or Oracle.
- Text Editor or IDE: Choose a code editor or integrated development environment (IDE) of your preference.

# Setting Up Your Django Project

Creating a new Django project and a new app within that project. In terminal run the following commands:
django-admin startproject 'project_name'
cd 'project_name'
python manage.py startapp 'app_name'

# Application Registration 

configure the settings.py file

Make sure the app (app_name) is included in the INSTALLED_APPS list:

    INSTALLED_APPS = [
        # ...
        'my_app',
    ]
# Defining Models

In Django, models are Python classes that define the structure of your database tables.
Creating a model for the tasks in myapp/models.py

# Create the models
class Task(models.Model)
  
-  create the database tables for models. 
 - Run the following commands to create the migrations and apply them:

python manage.py makemigrations
python manage.py migrate
Creating Forms

    
    class TaskForm(forms.ModelForm):
        class Meta:
            model = Tasks
            fields = '__all__'
            }
        
- Creating Function-Based Views

- Function-based create views for creating, reading, updating, and deleting tasks.


# Create the views

In this project, we handle both GET and POST requests. 
- If it's a GET request, we render a form for creating a new task.
If it's a POST request, we validate the form data and save the new task if it's valid.

- Read and Create Tasks (Dashboard view)


- Update a Task (Update View) 


- Delete a Task (Delete View) 


# Creating Templates

Create HTML templates for the views in the project templates directory. 
- base.html: CSS and editable page to custom view of all other pages.
- index.html: base page of app.
- sign-in.html: sign-in form.
- log-in.html: log-in form.
- tasks.html: create and update forms. 
- dashboard.html: listing, creating and updating tasks.
- update-task.html: update form.
- delete-task.html: delete form.


# Wiring Up URLs

- Configure the URLs for the views.

- Define the URLs for the views

# Testing Your CRUD Project

With everything set up, start your Django development server:
python manage.py runserver

# Final DJANGO App
You should be able to create, read, update, and delete orders in your Django CRUD project using function-based views.
