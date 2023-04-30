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


ToDo
----

StudentList
StudentDetail
StudentInterestsView

these need Student model.