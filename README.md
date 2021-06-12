# learn-django

## This is where I build projects while learning *Django* from different resources

### Index of resources and projects

* **[Django for beginners](https://djangoforbeginners.com/) book**
  * **[Hello World App](https://github.com/OmarKimo/learn-django/tree/main/helloworld): a *Django* project that simply says “Hello, World” on the homepage.**

  * **[Pages App](https://github.com/OmarKimo/learn-django/tree/main/pages): a *Django* project with a homepage and about page.**
  
  * **[Message Board App](https://github.com/OmarKimo/learn-django/tree/main/messageboard): a basic Message Board application where users can post *(through admin)* and read short messages.**
  
  * **[Blog App](https://github.com/OmarKimo/learn-django/tree/main/blog): a Blog application that allows users to create, edit, and delete posts.**

  * **[Newspaper App](https://github.com/OmarKimo/learn-django/tree/main/news): an articles page where journalists can post articles, set up permissions so only the author of an article can edit or delete it, and finally add the ability to write comments *(through admin)* on each article.**

* **[*Django 3.1* documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) tutorial**

  * **[Polls App](https://github.com/OmarKimo/learn-django/tree/main/djangofirst): a basic poll application.**
    > open through <http://127.0.0.1:8000/polls/> after running [these steps](https://github.com/OmarKimo/learn-django#you-can-run-any-web-app-by-executing-these-commands-in-its-corresponding-folder)
  
  * **[*django-polls* Package](https://github.com/OmarKimo/learn-django/tree/main/django-polls): a standalone Python package from poll web app you can reuse in new projects.**

* **[Django for APIs](https://djangoforapis.com/) book**

  * **[Library App & API](https://github.com/OmarKimo/learn-django/tree/main/library): a basic Library website with traditional *Django* and extend it into a web API with *Django REST Framework*.**
  
  * **[Todo API](https://github.com/OmarKimo/learn-django/tree/main/todo/backend): a Todo API back-end.**
  
  * **[Todo Frontend with React](https://github.com/OmarKimo/learn-django/tree/main/todo/frontend): a Todo Frontend built with React and connected to the Todo API.**
  
  * **[Blog API](https://github.com/OmarKimo/learn-django/tree/main/blogapi): a Blog API using the full set of *Django REST Framework* features such as users, permissions, full CRUD (Create-Read-Update-Delete) functionality, Schemas using *OpenAPI*, and API documentation using [*drf-yasg*](https://drf-yasg.readthedocs.io/en/stable/) package.**
    * **For the schema, you can open <http://127.0.0.1:8000/openapi/>**
    * **For the documentation, you can open <http://127.0.0.1:8000/swagger/> or <http://127.0.0.1:8000/redoc/>**

* **[*Django Rest Framework* documentation](https://www.django-rest-framework.org/tutorial/1-serialization/) tutorial**

  * **[Pastebin Code Highlighting API](https://github.com/OmarKimo/learn-django/tree/main/drf-tutorial)**
  
#### You can run any web app by executing these commands in its corresponding folder

##### 1. `python manage.py migrate`

##### 2. `python manage.py makemigrations`

##### 3. `python manage.py runserver`

##### After that you can open the website on <http://127.0.0.1:8000/>

#### And if you want to access the admin page, you must run `python manage.py createsuperuser` first
