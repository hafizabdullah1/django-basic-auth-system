# Django Basic Auth System

This repository contains a basic authentication system built using Django. The system includes essential features such as user login, signup, change password, and reset password.

## Features

- **Login**: Users can log in to their accounts using their credentials.
- **Signup**: New users can create an account by providing necessary information.
- **Change Password**: Logged-in users can change their password.
- **Reset Password**: Users can reset their password if they forget it.

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hafizabdullah1/django-basic-auth-system.git
   cd django-basic-auth-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to see the application.

## Usage

- **Login**: Navigate to `/accounts/login/` to access the login page.
- **Signup**: Navigate to `/accounts/signup/` to access the signup page.
- **Change Password**: Navigate to `/accounts/password_change/` (available after logging in).
- **Reset Password**: Navigate to `/accounts/password_reset/` to reset your password.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.

---

Feel free to modify and extend this basic auth system to fit your specific needs.

---

Happy coding! 🎉
