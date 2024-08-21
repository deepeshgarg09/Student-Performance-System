# Student Performance System

A Django-based web application to track and manage student performance. This project includes features for user authentication, viewing and managing student marks, and displaying the highest scorers.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Running the Project](#running-the-project)
4. [Testing](#testing)
5. [Contributing](#contributing)
6. [License](#license)

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

## Testing

To run the tests, use the following command:

```bash
python manage.py test
