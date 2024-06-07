# Projet-Ouanis
Entretien du projet OUANIS


#Front-end 
git pull to get the things
install les bibls : npm i 
run the svelte : npm run dev -- --open


#back-end/mysite

git pull to get the things
python -m pip install --upgrade pip     for upgrading pip
pip install -r requirements.txt      for installing the requirements
pip install django-cors-headers 
    for connectioing the databases i guess

py manage.py makemigrations 
py manage.py migrate 
py manage.py createsuperuser 
python manage.py runserver 



# En Voyage Admin Panel

Welcome to the En Voyage Admin Panel project. This project is a Django-based application designed to manage various aspects of the En Voyage platform, including user management, announcement handling, and more.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The En Voyage Admin Panel provides an interface for administrators to manage users, announcements, requests, and more. It is built with Django and includes a customized admin interface using Jazzmin for a better user experience.

## Features

- User Registration and Authentication
- Password Reset Functionality
- CRUD operations for Announcements, Requests, Tags, and more
- Customized Admin Interface with Jazzmin
- RESTful API with Token Authentication
- CORS support

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 5.0.2
- pip (Python package installer)
- A suitable database (SQLite, PostgreSQL, MySQL, etc.)

### Installation Steps

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
Create a Virtual Environment:

sh
Copier le code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:

sh
Copier le code
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the project root directory and add the following:

env
Copier le code
SECRET_KEY=your_secret_key
EMAIL_HOST_PASSWORD=your_email_password
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1  # Add your domain for production
Apply Migrations:

sh
Copier le code
python manage.py migrate
Create a Superuser:

sh
Copier le code
python manage.py createsuperuser
Run the Development Server:

sh
Copier le code
python manage.py runserver
Environment Variables
Ensure you have the following environment variables set in your .env file:

SECRET_KEY: Django secret key for your application.
EMAIL_HOST_PASSWORD: Password for your email host user.
DEBUG: Set to True for development and False for production.
ALLOWED_HOSTS: Comma-separated list of hosts allowed to serve the application.
Usage
Access the admin panel at http://localhost:8000/admin
Use the created superuser credentials to log in.
Manage users, announcements, and other models via the admin interface.
API Endpoints
The application provides several API endpoints for interacting with the models. Some of the key endpoints include:

POST /register/: Register a new user.
POST /login/: Log in a user and obtain a token.
GET /utilisateurs/: List all users.
GET /annonces/: List all announcements.
POST /reset_password/: Request a password reset.
Refer to the urls.py and views.py files for more details on available endpoints and their usage.

Customization
Admin Interface Customization
The admin interface uses Jazzmin for enhanced UI. You can further customize it by modifying the JAZZMIN_SETTINGS in settings.py.

Static and Media Files
Static files are served from the static directory.
Media files are uploaded to the media directory.
Ensure the paths are correctly set up in the settings.py:

python
Copier le code
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

Fork the repository.
Create a new branch: git checkout -b feature-branch
Make your changes and commit them: git commit -m 'Add some feature'
Push to the branch: git push origin feature-branch
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

rust
Copier le code

This README file provides a comprehensive overview of the project, instructio