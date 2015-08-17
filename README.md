# codango
Codango is a resource Sharing Social Network for Coders

#Installation
1. Clone the repository into a Virtual Environment. Run `virtualenv <virtualenvname>` to create the virtual environment.
2. Install all the necessary requirements by running `pip install -r requirements.txt` within the virtual environment.
3. Configure your database setting in _codango/settings.py_.
4. Run `python manage.py migrate` to create the user tables and everything required to run the application.
5. Run `python manage.py runserver` to run the app.
