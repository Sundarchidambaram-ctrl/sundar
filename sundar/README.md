# Django Ecommerce Project

A simple Django-based ecommerce application with product listings, shopping cart functionality, and basic admin interface.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/sundar.git
   cd sundar
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Main site: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Features

- Product listing and detail pages
- Shopping cart with add/remove/quantity update
- Django admin interface for managing products
- Session-based cart storage

## Project Structure

```
sundar/              # Project package
├── settings.py      # Django settings
├── urls.py          # Project URLs
├── wsgi.py          # WSGI app
└── asgi.py          # ASGI app

store/               # Main app
├── models.py        # Product model
├── views.py         # Views for products & cart
├── urls.py          # App URLs
├── admin.py         # Admin configuration
├── templates/       # HTML templates
└── static/          # CSS, JS, images
```

## Requirements

- Python 3.8+
- Django 4.2+

## License

MIT
