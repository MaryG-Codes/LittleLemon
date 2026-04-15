# Little Lemon Restaurant Management System

A Django-based restaurant management application for handling bookings, menu management, and customer interactions.

## Project Overview

Little Lemon is a web application built with Django that allows restaurant staff to manage reservations and display menu items to customers. The application includes features for table reservations, menu management, and a customer-facing interface.

## Features

- **Table Reservations**: Customers can book tables with name, date, and time slot selection
- **Menu Management**: Dynamic menu system with item descriptions and pricing
- **Booking Management**: View all reservations with date filtering
- **Responsive Design**: Template-based frontend with CSS styling
- **Database**: MySQL backend for persistent data storage

## Tech Stack

- **Framework**: Django 4.1.1
- **Database**: MySQL
- **Python**: 3.14
- **Frontend**: HTML/CSS Templates
- **ORM**: Django ORM

## Project Structure

```
littlelemon/
├── littlelemon/              # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py              # URL routing
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
├── restaurant/              # Main application
│   ├── models.py            # Database models (Booking, Menu)
│   ├── views.py             # Request handlers
│   ├── forms.py             # Django forms
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Django admin configuration
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── menu.html
│   │   ├── menu_item.html
│   │   ├── book.html
│   │   ├── bookings.html
│   │   ├── base.html
│   │   └── partials/        # Reusable template components
│   │       ├── _header.html
│   │       └── _footer.html
│   └── static/              # Static assets
│       ├── css/
│       │   └── style.css
│       └── img/
│           └── menu_items/
├── static/                  # Project-level static files
├── manage.py                # Django management command
└── Pipfile                  # Python dependencies
```

## Installation

### Prerequisites
- Python 3.14
- MySQL server
- pip and pipenv

### Setup Steps

1. **Clone/Navigate to the repository**
   ```bash
   cd littlelemon
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   ```

3. **Configure database**
   - Update the database configuration in `littlelemon/settings.py` with your MySQL credentials
   - Default configuration expects a local MySQL instance

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`

## Database Models

### Booking Model
Stores table reservation information:
- `first_name`: Customer name (max 200 chars)
- `reservation_date`: Date of reservation
- `reservation_slot`: Time slot (1-10, default: 10)

### Menu Model
Stores menu item information:
- `name`: Item name (max 200 chars)
- `price`: Item price
- `menu_item_description`: Detailed description (max 1000 chars)

## Available Views

| URL | View | Purpose |
|-----|------|---------|
| `/` | `home` | Homepage |
| `/about/` | `about` | About page |
| `/book/` | `book` | Booking form |
| `/reservations/` | `reservations` | View all bookings |
| `/menu/` | `menu` | Display full menu |
| `/menu_item/<id>/` | `display_menu_item` | View individual menu item |
| `/bookings/` | `bookings` | API endpoint for bookings |

## Usage

### Creating a Booking
1. Navigate to `/book/`
2. Fill in the booking form with customer name, date, and time slot
3. Submit the form

### Managing Menu
Access the Django admin interface at `/admin/` to:
- Add/edit/delete menu items
- Manage menu item descriptions and prices

### Viewing Reservations
- Navigate to `/reservations/` to view all bookings
- Use the date filter to view bookings for specific dates

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
When models are modified:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin
Access the admin interface at `http://localhost:8000/admin/` with superuser credentials to manage:
- Users and permissions
- Menu items
- Reservations

## Security Notes

⚠️ **Important for Production**:
- Change `SECRET_KEY` in settings.py before deployment
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` appropriately
- Use environment variables for sensitive configuration
- Never commit secrets to version control

## Future Enhancements

- User authentication for customers
- Email notifications for bookings
- Payment integration
- Online menu reviews/ratings
- Staff management system
- Inventory tracking

## License

This project is provided as-is for educational purposes.

