# Building a Django CRUD (Create, Retrieve, Update and Delete) Project 

Django is a powerful Python web framework that simplifies web development by providing a clean and pragmatic design. 



- Python and Django: Ensure you have Python installed on your system. You can install Django using pip:
pip install django
- Database: Decide on the database you want to use. 
- By default, Django uses SQLite, but you can configure it to use other databases like PostgreSQL, MySQL, or Oracle.

Text Editor or IDE: Choose a code editor or integrated development environment (IDE) of your preference.

# Setting Up Your Django Project

creating a new Django project and a new app within that project. In terminal run the following commands:
django-admin startproject 'project_name'
cd 'project_name'
python manage.py startapp 'app_name'

# Application Registration: configure the settings.py file

Make sure the app (app_name) is included in the INSTALLED_APPS list:

INSTALLED_APPS = [
    # ...
    'my_app',
]
# Defining Models

In Django, models are Python classes that define the structure of your database tables.
Creating a model for the tasks in myapp/models.py:


# Create the models.
class Task(models.Model):
  
 create the database tables for models. 
 - Run the following commands to create the migrations and apply them:

python manage.py makemigrations
python manage.py migrate
Creating Forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

        }
Creating Function-Based Views

Function-based create views for creating, reading, updating, and deleting tasks.

Create a Order (Create View) In crudapp/views.py, define a view function for creating a new order:

# Create the views.

In this project, we handle both GET and POST requests. 
If it's a GET request, we render a form for creating a new task
. If it's a POST request, we validate the form data and save the new order if it's valid.

- Read Orders (Dashboard view)


- Update a Order (Update View) 


- Delete a Order (Delete View) 


# Creating Templates

Now, create HTML templates for the views in the crudproject/templates directory. You'll need templates for the following views:

layout.html: for creating base html file with navbar.

Similarly, create HTML templates for the views in the crudproject/templates/crudapp directory. You'll need templates for the following views:

order.html: For the create and update forms. show.html: For listing all orders. confirmation.html: For confirming order deletion.


Add Bootstrap Crispy forms for styling form and navbar

Wiring Up URLs

Finally, configure the URLs for your views. In your project's crudproject/urls.py file, include the URLs for the crudapp app:


]
Then, in your app's crudpp/urls.py file, define the URLs for your views:

]
Testing Your CRUD Project

With everything set up, you can start your Django development server:

python manage.py runserver
 and you should be able to create, read, update, and delete orders in your Django CRUD project using function-based views.

how to create a Django CRUD project using function-based views. You can further enhance your project by adding features like authentication,
pagination, or search functionality. Django's flexibility and extensive ecosystem make it a great choice
