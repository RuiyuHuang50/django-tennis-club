# My Tennis Club - Django Project

This is a Django web application for managing a tennis club's members. This project follows the [W3Schools Django Tutorial](https://www.w3schools.com/django/).

## Features

- Member management system
- List all members
- View individual member details
- Django admin interface for easy data management
- Responsive HTML templates

## Project Structure

```
my_tennis_club/
├── manage.py
├── my_tennis_club/           # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── members/                  # Members app
    ├── models.py            # Member model
    ├── views.py             # View functions
    ├── urls.py              # URL patterns
    ├── admin.py             # Admin configuration
    └── templates/           # HTML templates
        ├── main.html
        ├── all_members.html
        ├── details.html
        ├── master.html
        └── template.html
```

## Models

### Member Model
- `firstname` - Member's first name
- `lastname` - Member's last name  
- `phone` - Contact phone number
- `joined_date` - Date when member joined

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RuiyuHuang50/django-tennis-club.git
   cd django-tennis-club
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv myworld
   source myworld/bin/activate  # On Windows: myworld\Scripts\activate
   ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Main page: `http://127.0.0.1:8000/`
   - Members list: `http://127.0.0.1:8000/members/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## URLs

- `/` - Home page
- `/members/` - List all members
- `/members/details/<id>/` - View member details
- `/testing/` - Template testing page
- `/admin/` - Django admin interface

## Templates

The project uses Django's template inheritance system:
- `master.html` - Base template
- `main.html` - Home page
- `all_members.html` - Members listing
- `details.html` - Member details
- `template.html` - Testing template with loops

## Learning Resource

This project was built following the comprehensive Django tutorial at [W3Schools Django](https://www.w3schools.com/django/), which covers:
- Django installation and setup
- Creating projects and apps
- Models and databases
- Views and templates
- URL routing
- Django admin
- And much more!

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is for educational purposes following the W3Schools Django tutorial.