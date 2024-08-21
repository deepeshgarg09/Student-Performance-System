# Student Performance System

A Django-based web application to track and manage student performance. This project includes features for user authentication, viewing and managing student marks, and displaying the highest scorers.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Running the Project](#running-the-project)
4. [Adding Data](#adding-data)
5. [Using the Admin Interface](#using-the-admin-interface)
6. [Workflow](#workflow)
7. [Testing](#testing)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set Up PostgreSQL Database**

    Create a PostgreSQL database and user. Update the `DATABASES` setting in `your_project/settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

2. **Configure Redis**

    Update the `CACHES` setting in `your_project/settings.py`:

    ```python
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
    ```

## Running the Project

1. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

## Adding Data

### Adding Students

1. Navigate to the `Register` page:

    URL: `/register/`

2. Fill in the registration form with student details and submit.

### Adding Subjects

1. Navigate to the Django Admin Interface:

    URL: `/admin/`

2. Log in with your superuser account.
3. Go to the `Subjects` section.
4. Click `Add Subject`, fill in the details, and save.

### Adding Marks

1. Navigate to the Django Admin Interface:

    URL: `/admin/`

2. Log in with your superuser account.
3. Go to the `Marks` section.
4. Click `Add Marks`, select the student and subject, enter the marks obtained, and save.

## Using the Admin Interface

1. **Access Admin Interface**

    Navigate to `/admin/` on your local server (e.g., `http://localhost:8000/admin/`).

2. **Log In**

    Use the superuser credentials created earlier.

3. **Admin Roles and Capabilities**

    - **Users**: Admins can view, add, edit, or delete user accounts. This includes managing student accounts and updating user details.
    - **Subjects**: Admins can view, add, edit, or delete subjects. This allows for the management of the list of subjects available for students.
    - **Marks**: Admins can view, add, edit, or delete marks records. This functionality is crucial for managing student performance data.

## Workflow

1. **Registration**: Users can register through the `Register` page.

    URL: `/register/`

2. **Login**: Users log in using their credentials. They are redirected to the `Dashboard` page upon successful login.

    URL: `/login/`

3. **Dashboard**: Authenticated users can view their marks, the highest scorer for each subject, and the overall highest scorer.

    URL: `/dashboard/`

4. **Logout**: Users can log out from the `Dashboard` page, which will redirect them to the login page.

    URL: `/logout/`

## Testing

To run the tests, use the following command:

```bash
python manage.py test
