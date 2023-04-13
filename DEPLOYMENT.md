# DEPLOYMENT
## Table of Contents
- ### [Initial Deployment](#initial-deployment)
    - [Create Repository](#create-repository)
    - [Setting up the Workspace (To be done locally via the console of your chosen editor)](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    - [Create Heroku App](#create-heroku-app)
    - [AWS S3 Bucket](#aws-s3-bucket)
    - [Creating Environmental Variables Locally](#creating-environmental-variables-locally)
    - [Setting up setting.py File](#setting-up-settingpy-file)
    - [Set up Heroku for use via the console](#set-up-heroku-for-use-via-the-console)


## Initial Deployment
Below are the steps taken to deploy the site to Heroku and any console commands required to initiate it.
- ## Create Repository
    1. Create a new repository in GitHub and clone it locally by <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository" target="_blank">following these instructions</a>
        - Note - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
            - pip install -r requirements.txt
        - IMPORTANT - If developing locally on your device, ensure you set up/activate the virtual environment (see below) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk

## Setting up the Workspace (To be done locally via the console of your chosen editor)
    1. Create a virtual environment on your machine (Can be skipped if using gitpod):
        - python -m venv .venv
    2. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
    3. Install Django with version 3.2:
        - pip install django==3.2.14
    4. Install gunicorn:
        - pip install gunicorn
    5. Install supporting libraries:
        - pip install dj_database_url
        - pip install psycopg2-binary
    6. Create requirements.txt:
        - pip freeze --local > requirements.txt
    7. Create an empty folder for your project in your chosen location.
    8. Create a project in the above folder:
        - django-admin startproject <PROJECT_NAME> 
    9. Create an app within the project:
        - python manage.py startapp APP_NAME
    10. Add a new app to the list of installed apps in setting.py
    11. Migrate changes:
        - python manage.py migrate
    12. Test server works locally:
        - python manage.py runserver

## Create Heroku App
The below works on the assumption that you already have an account with Heroku and are already signed in.
1. Create a new Heroku app:
    - Click "New" in the top right-hand corner of the landing page, then click "Create new app."
2. Give the app a unique name:
    - Will form part of the URL 
3. Select the nearest location:
For me, this was Europe.
4. Add Database to the Heroku app:
    - Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears.
    - Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
5. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    - left box under config vars (variable KEY) = SECRET_KEY
    - right box under config vars (variable VALUE) = Value copied from settings.py in project.


## AWS S3 BUCKET
The below works on the assumption that you already have an account with AWS and are already signed in.
1. Create a new S3 bucket:
    - Click "Services" in the top left-hand corner of the landing page, click on "Storage" then click "S3."
    - Click "Create bucket."
    - Give the bucket a unique name:
        - Will form part of the URL (in the case of this project, I called the S3 bucket gregmediscrubs)
    - Select the nearest location:
    - Under the "Object Ownership" section, select "ACLS enabled"
    - Under the "Block Public Access settings for this bucket" section, untick "Block all public access" and tick the box to acknowledge that this will make the bucket public.
    - Click "Create bucket."
2. Amend Bucket settings:
    - Bucket Properties: -
        - Click on the bucket name to open the bucket.
        - Click on the "Properties" tab.
        - Under the "Static website hosting" section, click "Edit."
        - Under the "Static website hosting" section select "Enable".
        - Under the "Hosting type" section ensure "Host a static website" is selected.
        - Under the "Index document" section enter "index.html".
        - Click "Save changes."
    - Bucket Permissions: -
        - Click on the "Permissions" tab.
        - Scroll down to the "CORS configuration" section and click edit.
        - Enter the following snippet into the text box:       
           ``` [
                {
                    "AllowedHeaders": [
                    "Authorization"
                    ],
                    "AllowedMethods": [
                    "GET"
                    ],
                    "AllowedOrigins": [
                    "*"
                    ],
                    "ExposeHeaders": []
                }
            ] 
            ```
        - Click "Save changes."
        - Scroll back up to the "Bucket Policy" section and click "Edit."
        - Take note of the "Bucket ARN" click on the "Policy Generator" button to open the AWS policy generator in a new tab.
        - In the newly opened tab under Step 1 "Select Policy Type" select "S3 Bucket Policy." from the drop down menu.
        - Under Step 2 "Add Statement(s)" enter " * " in the "Principal" text box.
        - From the "s3:Action" drop down menu select "s3:GetObject".
        - Enter the "ARN" noted from the bucket policy page into the "Amazon Resource Name (ARN)" text box.
        - Click "Add Statement."
        - Under Step 3 "Generate Policy" click "Generate Policy."
        - Copy the resultant policy and paste it into the bucket policy text box on the previous tab.
        - In the same text box add "/*" to the end of the resource key to allow access to all resources in this bucket.
        - Click "Save changes."
        - When back on the buckets permissions tab, scroll down to the "Access Control List" section and click "Edit."
        - enable "List" for "Everyone (public access)", tick the box to accept that "I understand the effects of these changes on my objects and buckets." and click "Save changes."
3. Create AWS static files User and assign to S3 Bucket:
    - Create "User Group": -
        - Click "Services" in the top left-hand corner of the landing page, from the left side of the menu click on "Security, Identity, & Compliance" and select "IAM" from the right side of the menu.
        - Under "Access management" click "User Groups."
        - Click "Create Group."
        - Enter a user name (in the case of this project, I called the user group "manage-gregmediscrubs").
        - Scroll to the bottom of the page and click "Create Group."
    - Create permissions policy for the new user group: -
        - Click "Policies" in the left-hand menu.
        - Click "Create Policy."
        - Click "Import managed policy."
        - Search for "AmazonS3FullAccess", select this policy, and click "Import".
        - Click "JSON" under "Policy Document" to see the imported policy
        - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
        - Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.
        - Click "Next: Tags."
        - Click "Next: Review."
        - Click "Review Policy."
        - Enter a name for the policy (in the case of this project, I called the policy "gregmediscrubs").
        - Enter a description for the policy.
        - Click "Create Policy."
    - Attach Policy to User Group: -
        - Click "User Groups" in the left-hand menu.
        - Click on the user group name created during the above step.
        - Select the "Permissions" tab.
        - click "Attach Policy."
        - Search for the policy created during the above step, and select it.
        - Click "Attach Policy."
    - Create User: -
        - Click "Users" in the left-hand menu.
        - Click "Add user."
        - Enter a "User name".
        - Select "Programmatic access" and "AWS Management Console access."
        - Click "Next: Permissions."
        - Select "Add user to group."
        - Select the user group created during the above step.
        - Click "Next: Tags."
        - Click "Next: Review."
        - Click "Create user."
        - Take note of the "Access key ID" and "Secret access key" as these will be needed to connect to the S3 bucket.
        - Click "Download .csv" to download the credentials.
        - Click "Close."
4. Install required packages to used AWS S3 Bucket in Django:
    - pip install boto3
    - pip install django-storages
5. Add 'storages' to the bottom of the installed apps section of settings.py file:
```
 INSTALLED_APPS = [
 …,
     'storages'
 …,
]
```

## Creating Environmental Variables Locally
1. Install dotenv package:
    - pip install python-dotenv
2. On your local machine, create a file called ".env" at the same level as settings.py and add this to the .gitignore file.
3. From your projects settings.py file, copy the SECRET_KEY value and assign it to a variable called SECRET_KEY in your .env file
    - SECRET_KEY=PastedValueFromYourProjectsSettings.pyFile
4. Add DEVELOPMENT variable to .env file:
    - DEVELOPMENT=development

## Setting up setting.py File
1. At the top of your settings.py file, add the following snippet:
```
import os
import dj_database_url
from pathlib import Path

if os.path.exists("env.py"):
    import env

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = 'DEVELOPMENT' in os.environ
```
2. Add a conditional in setting.py DATABASES section by replacing it with the following snippet to link up the Heroku Postgres server when in production and SQLite3 when developing locally:
```
if 'DATABASE_URL' in os.environ:
   DATABASES = {
       'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
   }
else:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
```
3. 
```
# Static files (CSS, JavaScript, Images)
   # https://docs.djangoproject.com/en/3.2/howto/static-files/
   STATIC_URL = '/static/'
   STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
4. Import setting and static functions into the project settings.py file:
```
from django.conf import settings
   from django.conf.urls.static import static
```
5. Add the following snippet to the end of the urlpatterns list:
```
 urlpatterns =[
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
6. Under the line with BASE_DIR, link templates directly in Heroku via settings.py:

    - TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
7. Within TEMPLATES array, add 'DIRS':[TEMPLATES_DIR] like the below example:
```
TEMPLATES = [
       {
           …,
           'DIRS': [TEMPLATES_DIR],
           …,
          
        },
   ]
```
8. Link S3 Bucket to Django Project by adding the following to the settings.py file:
```
# its important to keep the AWS keys secret so we use environment variables which will be added to Heroku later
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
       'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
       'CacheControl': 'max-age=94608000',
    }
    # Bucket config
    AWS_STORAGE_BUCKET_NAME = '{Bucket name}' # name of your bucket
    AWS_S3_REGION_NAME = '{Region name}' # region of your bucket
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
9. Add allowed hosts to settings.py:
    - ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost", "127.0.0.1"]
10. Create Procfile at the top level of the file structure and insert the following:
    - web: gunicorn PROJECT_NAME.wsgi
11. Make an initial commit and push the code to the GitHub Repository.
    - git add .
    - git commit -m "Initial deployment"
    - git push
12. Add AWS Keys from step 7 above to Heroku Config Vars.
13. Add the USE_AWS variable to Heroku Config Vars and set it to True.
14. Create a file call "Custom_storages.py" in the root of the project and add the following code:
```
# this file is used to tell Django where to store static and media files when COLLECT_STATIC is run (when deploying to heroku)
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION

    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
```

### Set up Heroku for use via the console

1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the API key.
3. Log in to Heroku via the console and enter your details.
    - heroku login-i
    - When prompted, enter your Heroku username
    - Enter copied API key as the password   
4. Get your app name from Heroku
    - heroku apps
5. Set Heroku remote
    - heroku git:remote -a <app_name>
6. Add, Commit, Pust to GitHub:
    - git add . && git commit -m "Deploy to Heroku via CLI"
7. Push to GitHub and Heroku
    - git push origin main
    - git push heroku main

- [Back to top](#table-of-contents)
- [Back to Readme.md](./README.md)