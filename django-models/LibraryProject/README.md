# Learn Django Framework

## Project overview

LibraryProject is a small Django application that demonstrates common patterns for building a library/catalog system: models for books and authors, admin integration, basic search and list/detail views, and a simple checkout/reservation workflow.

## Features

- Book, Author and Genre models
- Browsable list and detail pages
- Admin site configuration for content management
- Basic search and filtering
- REST-ish endpoints (optional)
- Tests for core functionality

## Requirements

- Python 3.8+
- Django 3.2+ (or the version pinned in requirements.txt)
- pip

## Quick start

1. Clone the repository

   - git clone <repo-url>
   - cd LibraryProject

2. Create and activate a virtual environment

   - python -m venv venv
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate

3. Install dependencies

   - pip install -r requirements.txt

4. Apply migrations and create a superuser

   - python manage.py migrate
   - python manage.py createsuperuser

5. Run the development server
   - python manage.py runserver
   - Open http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/

## Configuration

- Default config uses SQLite (settings.py). To use Postgres or another DB, update DATABASES in settings or set environment variables.
- For environment-specific secrets, create a .env and load values with django-environ or your preferred method.
- Important settings:
  - SECRET_KEY
  - DEBUG
  - DATABASE_URL

## Running tests

- Run unit tests:
  - python manage.py test

## Project structure (high level)

- manage.py
- config/ (project settings, urls, wsgi/asgi)
- library/ (app: models, views, urls, serializers)
- templates/
- static/
- requirements.txt

## Development tips

- Use the admin to quickly create authors and books.
- Use Django shell for quick data checks: python manage.py shell
- Add new app-specific migrations with: python manage.py makemigrations

## Contributing

- Fork the repository, create a feature branch, and open a pull request.
- Write tests for new features and ensure existing tests pass.
- Follow PEP 8 and include a concise PR description.

## License

This project is provided under the MIT License. See LICENSE for details.

## Contact

For questions or contributions, open an issue or pull request in the repository.
