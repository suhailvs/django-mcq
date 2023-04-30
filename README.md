# django-quiz


Installation
------------
Install django-quiz

Run `pip install django-quiz`.

Add `'quiz'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'quiz',
        ...
    )

Add the following to your projects `urls.py` file.


    urlpatterns = [
        ...
        path('quiz/', include('quiz.urls')),
    ]


Create a template `quiz_base.html` file in **templates** folder:

    <!doctype html>
    <html lang="en">
        <head>
            {% block quiz_css %}{% endblock %}
        </head>
        <body>
            {% block quiz_body %}{% endblock %}
            {% block quiz_js %}{% endblock %}
        </body>
    </html>