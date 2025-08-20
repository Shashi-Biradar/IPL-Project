# 🏏IPL Management System with Authentication (Python + MySQL + SQLAlchemy ORM)

A Python-based IPL Management System with user authentication (Signup/Login) using MySQL database and SQLAlchemy ORM.
This project allows authenticated users to perform CRUD (Create, Read, Update, Delete) operations on IPL teams and players.
With ORM, all database operations are written in a Pythonic, object-oriented way, avoiding raw SQL queries.

🚀 Features
🔐 Authentication

User Signup with username & password

Secure Login with hashed passwords

Each user has their own records

🏏 IPL CRUD Operations

📥 Create – Add new IPL teams and players

📋 Read – View all teams and players

✏️ Update – Edit team or player details

❌ Delete – Remove team or player

🔎 Search – Find players by name, team, or role

📊 ORM Advantages

Uses SQLAlchemy ORM (object-oriented DB handling)

Easy migration between databases (SQLite → MySQL → PostgreSQL)

Clean models for User, Team, Player

🛠️ Tech Stack

Language: Python 3

Database: MySQL

Libraries:

SQLAlchemy → ORM

pymysql → MySQL connector for Python

SQLite Viewer → Pretty table output

hashlib → Password hashing

📂 Project Structure
ipl-orm-mysql-project/
│── models.py           # SQLAlchemy models (User, Team, Player)
│── ipl_manager.py      # Main program file (Authentication + CRUD logic)
│── README.md           # Project documentation