### Steps taken to creatae this webapp:
1. Verify supported technology is installed:
    * Python 3.5.x
    * Django
    * Postgres (Database)
    * Whitenoise (For static files)
    * See requirements.txt for full details here
	* PGAdmin 3 or 4
	* Existing Heroku account
	* Heroku CLI installed

**Instructions are based on a Windows 10 OS**

	1. $ virtualenv venv
	2. $ venv\Scripts\activate.bat
		a. To Deactcivate:
		b. $ venv\Scripts\deactivate.bat
	3. $ python C:\code\Personal\django-attendance-webapp\venv\Scripts\django-admin.exe startproject attendance
		a. Due to a bug in virtualenv on Windows you have to fully qualify the django-admin.exe path.
	4. Create .gitignore file:
		*.pyc
		.DS_Store
		*.swp
		venv
		/venv/
		/static/
		/media/
		.env
		.idea
		staticfiles
	5. Create/Updated requirements.txt to include other known needed packages
        * pip freeze > requirements.txt
        * pip install -r requriements.txt
    6. Convert settings.py to settings folder with `base.py', `dev.py`, and `production.py`
	7. Create repo and commit (Add Readme.MD)
	8. Update manage.py to look for .env file
	9. Prepare webapp for Heroku
	    * Create "Procfile" on line of code (point to app.wsgi.py):
	            `web: gunicorn attendance.wsgi`
	    * Update settings.py to work with .env file
	    * Convert project to postgres db
	        * Create postgres DB 'attendance'
	        * Delete `db.sqlite3` if it exists
	        * Update ".env" file with local variables:
	            * WEB_CONCURRENCY=2
                * DJANGO_SETTINGS_MODULE=attendance.settings.py
                * SECRET_KEY='***************************'
                * DB_USER_NAME='********'
                * DB_PASSWORD='********'
            * Update settings.py to use postgres instead of sqllight
    10. Migrate db:
          * $ python manage.py migrate
    11. Log into Heroku using cli
        * heroku login
    12. Create heroku app
        * heroku create myregistration
    13. Deploy to heroku
        * $ git push heroku master
        * $ heroku run python manage.py migrate
        * $ heroku run python manage.py createsuperuser
    14. Create events app inside django
        * $ python manage.py startapp events
    15. Update events app accodingly
        * Update urls.py (both)
        * Add app to "INSTALLED_APPS" settings.py
        * Create models
        * $ python manage.py makemigrations
        * $ python manage.py migrate
        * Create templates
        * Code veiws.py to work with templates and models to serve up pages
    16. Create registrations app
        * $ python manage.py startapp registrations