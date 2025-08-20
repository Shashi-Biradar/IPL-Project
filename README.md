# 🏏IPL Management System (Django + MySQL)

A Django-based web application for managing IPL teams and players with user authentication.
The project allows users to sign up, log in, and perform CRUD (Create, Read, Update, Delete) operations on IPL records.
Data is stored in a MySQL database, and Django’s ORM is used for database interaction.

🚀 Features
🔐 Authentication

User Signup/Login/Logout (Django auth system)

Each user manages their own records securely

🏏 IPL CRUD Operations

📥 Create – Add new IPL teams and players

📋 Read – View all teams and players

✏️ Update – Edit team or player details

❌ Delete – Remove team or player

🔎 Search – Find players by name, team, or role

🌐 Web Features

Django templates for frontend

Django ORM for database interaction

Admin panel for managing all records

🛠️ Tech Stack

Framework: Django 5 (or 4.x if you’re using older)

Language: Python 3

Database: MySQL

Libraries:

mysqlclient or pymysql → MySQL connector

Django built-in packages for auth, forms, ORM

📂 Project Structure
ipl-django-crud/
│── ipl_project/           # Main Django project folder
│   ├── settings.py        # Project settings (configure MySQL here)
│   ├── urls.py            # Root URL config
│── ipl_app/               # Django app for IPL management
│   ├── models.py          # Team & Player models
│   ├── views.py           # Business logic (CRUD + auth)
│   ├── urls.py            # App URL routing
│   ├── templates/         # HTML templates
│── manage.py              # Django project manager
│── README.md              # Documentation