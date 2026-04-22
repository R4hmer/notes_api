# Flask Notes API (User Authentication & Notes Tracker)

## Project Description

This is a RESTful API built with Flask that allows users to:

- Register and log in securely
- Create, read, update, and delete personal notes
- Ensure full data privacy between users
- Store authentication using session-based login
- Use pagination when retrieving notes

Each user can only access their own notes, ensuring complete data isolation and security.

## Features

- User authentication (Signup, Login, Logout)
- Session-based authentication
- Password hashing using Bcrypt
- User-owned Notes resource
- Full CRUD operations on notes
- Pagination support on GET /notes
- Protected routes (authentication required)
- Database migrations using Flask-Migrate

## Installation Instructions

### 1. Clone the repository

git clone <your-repo-url>
cd flask-notes-api

### 2. Create virtual environment and install dependencies
pipenv install
pipenv shell

### 3. Run the application
flask run

