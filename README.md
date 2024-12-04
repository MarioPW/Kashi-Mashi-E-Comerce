# Kashi-Mashi E-Comerce

## Description
This is a full-featured e-commerce website built with Django. The platform allows users to browse products, add items to their cart, and complete the checkout process. Admin users have access to the management interface for adding and updating products, categories, and orders.

## Features
- User authentication (sign-up, login, logout)
- Product catalog with categories
- Product detail pages
- Cart and checkout functionality
- Order tracking
- Admin dashboard for managing products, orders, and users

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap 5.1.3
- **Database**: PostgreSQL (can be changed to SQLite for development)
- **Payment Processing**: Stripe API
- **Environment Management**: Python virtual environment
- **Testing**: Django Test Framework
- **Images**: Cloudinary

## Requirements
- Python 3.7+
- Django 3.x+
- PostgreSQL 10+
- Stripe API key

# Installation
### 1. Clone the Repository
First, clone the repository from GitHub and navigate to the project folder:

```bash
git clone https://github.com/yourusername/your-ecommerce-project.git
cd your-ecommerce-project
```
### 2. Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to keep the project dependencies isolated:

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Install all required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
Create a .env file in the project's root directory to store environment variables. These variables configure services like databases, Cloudinary, or secret keys.

Example .env:
```.env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

# Cloudinary Configuration
CLOUD_NAME=your-cloud-name
API_KEY=your-api-key
API_SECRET=your-api-secret

# Other Configurations
ROOT_DOMAIN=http://127.0.0.1:8000
Notes:
SECRET_KEY: A unique key to secure your application; never share it publicly.
DEBUG: Should be set to True only in the development environment.
CLOUD_NAME, API_KEY, API_SECRET: Required if you're using Cloudinary to handle images.
```
### 5. Apply Migrations
Run migrations to set up the database:

```bash
python manage.py migrate
```
### 6. Create a Superuser
Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```
### 7. Run the Server
Start the development server:

```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser to see the application running.
# Folder Structure

```
Kashi-Mashi E-comerce/
├── store/              # Main Django project folder
│   ├── settings.py         # Django settings file
│   ├── urls.py             # URL routing for the project
│   ├── wsgi.py             # WSGI configuration for deployment
│   └── asgi.py             # ASGI configuration for async support
├── catalog/                # Products app for handling product-related and categories logic
│   ├── models.py           # Product and Category models
│   ├── views.py            # Views for product catalog, details, etc.
│   └── templates/          # HTML templates for product pages
├── cart/                   # Cart app for cart and checkout logic
│   └── ... TODO
├── orders/                 # Orders app for handling order management
│   └── ... TODO
├── home/                  # App for managing diferent pages in the website
│   ├── models.py           # Orders, Another_Equal, Payment_Methods, Frequent_Questions, Message, and Carousel_Stuff

│   ├── views.py            # Views for product orders, details, carousel, etc.
│   └── templates/
├── templates/              # Base HTML templates
└── requirements.txt        # Project dependencies
```