# EventNest - Event Management Platform

![EventNest Logo](https://img.shields.io/badge/Event-Nest-blue?style=for-the-badge&labelColor=3B82F6&color=10B981)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://eventnest00.pythonanywhere.com)

A comprehensive event management platform built with Django, designed for the Bangladesh market. EventNest connects users with professional event services including photography, catering, event management, and printing services.

## 🚀 Live Demo

**Website:** [https://eventnest00.pythonanywhere.com](https://eventnest00.pythonanywhere.com)

## 🌟 Features

### 🎯 Core Features
- **Service Booking System** - Book professional event services with date/time selection
- **E-commerce Store** - Purchase event-related products with cart & checkout
- **Wishlist** - Save favorite products for later
- **User Profiles** - Manage personal information and preferences
- **Notifications** - Real-time updates on bookings and orders
- **Search** - Find services and products quickly

### 📋 Service Categories
- 📸 **Photography** - Wedding, corporate, portrait photography
- 🍽️ **Catering** - Full-service catering for all events
- 🎉 **Event Management** - Complete event planning & coordination
- 🖨️ **Printing Services** - Invitations, banners, promotional materials

### 🛒 Store Features
- Product catalog with categories
- Shopping cart with quantity management
- Wishlist functionality
- Order history tracking
- Secure checkout process

### 👤 User Features
- User registration with phone validation (+880 format)
- Profile management
- Booking management (view, modify, cancel)
- Order tracking
- Notification center

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.13 | Backend language |
| Django | 5.2rc1 | Web framework |
| SQLite | 3 | Database |
| HTML/CSS | 5/3 | Frontend |
| Bootstrap Icons | 1.11 | Icons |
| JavaScript | ES6 | Interactivity |

## 📁 Project Structure

```
EventNest/
├── Main/
│   ├── core/                    # Main application
│   │   ├── models.py            # Database models
│   │   ├── views.py             # View functions
│   │   ├── forms.py             # Django forms
│   │   ├── context_processors.py # Template context
│   │   ├── templates/           # HTML templates
│   │   │   ├── base.html        # Base template
│   │   │   ├── home.html        # Homepage
│   │   │   ├── core/            # Core templates
│   │   │   ├── services/        # Service templates
│   │   │   ├── store/           # Store templates
│   │   │   └── registration/    # Auth templates
│   │   └── static/
│   │       ├── css/theme.css    # Custom styles
│   │       └── images/          # Static images
│   ├── media/                   # User uploads
│   ├── myproject/               # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── staticfiles/             # Collected static files
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

## 🚀 Installation

### Prerequisites
- Python 3.10 or 3.11 (recommended). Newer Python versions (3.13/3.14) may require building some binary wheels from source.
- pip (Python package manager)
- Git

### macOS system libraries (if using macOS)
Some Python packages (for example Pillow) require native image libraries to build. Install them with Homebrew if you see build errors for Pillow:

```bash
# install Homebrew first (if you don't have it): https://brew.sh/
brew install libjpeg libtiff webp zlib
```

### Setup Instructions (recommended)

1. Clone the repository and change into it:
```bash
git clone https://github.com/Prohar04/EventNest.git
cd EventNest
```

2. Work from the `Main/` folder where `manage.py` lives. Create a virtual environment and activate it:
```bash
cd Main
python3 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

3. (If you get an error like `Invalid requirement: 'D\x00j\x00a...')` the `requirements.txt` file is UTF-16 encoded. Convert it (one-time):
```bash
# from the repository root
python - <<'PY'
from pathlib import Path
p = Path('Main/requirements.txt')
b = p.read_bytes()
for enc in ('utf-16', 'utf-16-le', 'utf-16-be', 'utf-8'):
    try:
        s = b.decode(enc)
        p.write_text(s, encoding='utf-8')
        print('Re-encoded using', enc)
        break
    except Exception:
        pass
else:
    print('Could not decode requirements.txt; inspect file encoding')
PY
```

4. Upgrade packaging tools and install Python dependencies:
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

Notes:
- If `pip install` fails while building `Pillow`, install the macOS system libs (see above) or use Python 3.10/3.11 where prebuilt wheels are available.

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create an admin user:
```bash
python manage.py createsuperuser
```

7. (Optional) Populate sample data:
```bash
python populate_data.py
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Open the site in your browser:
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Troubleshooting tips
- If you see errors building wheels for packages like `Pillow`, prefer installing the OS image libraries via Homebrew (macOS) or the equivalent package manager on Linux, or use Python 3.10/3.11.
- If you prefer to run with a production DB or cloud host, set `DATABASE_URL` and other environment variables; see `Main/myproject/settings.py` for supported env vars.

## 📊 Database Models

### Core Models
| Model | Description |
|-------|-------------|
| `User` | Django built-in user model |
| `UserProfile` | Extended user information (phone, address) |
| `Service` | Base service model |
| `ServiceCategory` | Service categories |
| `Photography` | Photography service details |
| `Catering` | Catering service details |
| `EventManagement` | Event management details |
| `PrintingService` | Printing service details |

### E-commerce Models
| Model | Description |
|-------|-------------|
| `StoreItem` | Products in the store |
| `StoreCategory` | Product categories |
| `Cart` | User shopping cart |
| `CartItem` | Items in cart |
| `Order` | Completed orders |
| `OrderItem` | Items in order |
| `Wishlist` | User wishlist |

### Booking & Notifications
| Model | Description |
|-------|-------------|
| `Booking` | Service bookings |
| `Notification` | User notifications |
| `Contact` | Contact form submissions |

## 🔗 URL Endpoints

### Public Pages
| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/services/` | All services |
| `/services/<id>/` | Service detail |
| `/store/` | Product store |
| `/store/item/<id>/` | Product detail |
| `/search/` | Search results |
| `/contact/` | Contact form |

### Authentication
| URL | Description |
|-----|-------------|
| `/login/` | User login |
| `/signup/` | User registration |
| `/logout/` | User logout |

### User Dashboard
| URL | Description |
|-----|-------------|
| `/profile/` | User profile |
| `/my-bookings/` | User bookings |
| `/order-history/` | Order history |
| `/wishlist/` | User wishlist |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout page |
| `/notifications/` | Notifications |

### Booking Actions
| URL | Description |
|-----|-------------|
| `/book/<service_id>/` | Book a service |
| `/booking/modify/<id>/` | Modify booking |
| `/booking/cancel/<id>/` | Cancel booking |

## 🎨 UI/UX Features

- **Modern Dark Theme** - Professional dark color scheme
- **Responsive Design** - Works on all devices
- **EventNest Branding** - Event (blue) + Nest (green) logo
- **Status Timeline** - Visual booking status tracker
- **Real-time Notifications** - Dropdown notification panel
- **Bangladesh Localization** - BDT currency (৳), +880 phone format

## 🔒 Security Features

- CSRF protection on all forms
- Login required for sensitive pages
- Password hashing
- Session management
- Input validation

## 📝 Sample Data

The project includes scripts to populate sample data:
- **5 Users** (including admin)
- **61 Services** across all categories
- **42 Store Products**
- **Sample Bookings, Orders, and Notifications**

## 🧪 Testing

```bash
# Run Django system check
python manage.py check

# Run tests
python manage.py test core
```

## 📦 Dependencies

```
Django>=5.0
Pillow>=10.0
python-dotenv>=1.0
```

## 🌐 Deployment

The project includes configuration for Vercel deployment:
- `vercel.json` - Vercel configuration
- `wsgi_vercel.py` - WSGI for serverless

## 👥 Authors

- **Prohar** - [GitHub](https://github.com/Prohar04)

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Icons
- All contributors and testers
