# SteelGrid Systems - Industrial Engineering Website

A modern, production-ready website for SteelGrid Systems, showcasing industrial engineering services, projects, and expertise.

## Features

- Modern, responsive design with Bootstrap 5
- Server-side rendering with Django templates
- SEO optimized with meta tags and sitemap
- Blog system with rich text editing
- Project portfolio with filtering
- Team member profiles
- Contact form with validation
- Dark mode support
- Lazy loading images
- Scroll animations
- Production-ready security settings

## Tech Stack

- Django 5.0.2
- Bootstrap 5.3.2
- Font Awesome 6.0.0
- AOS (Animate On Scroll)
- CKEditor for rich text editing
- PostgreSQL (production) / SQLite (development)

## Prerequisites

- Python 3.8+
- Node.js and npm (for frontend dependencies)
- PostgreSQL (for production)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/steelgrid-systems.git
cd steelgrid-systems
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/macOS
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install frontend dependencies:
```bash
npm install
```

5. Create a `.env` file in the project root:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Collect static files:
```bash
python manage.py collectstatic
```

## Development

Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## Production Deployment

1. Update `.env` file with production settings:
```env
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

2. Install production dependencies:
```bash
pip install gunicorn psycopg2-binary
```

3. Set up PostgreSQL database

4. Configure your web server (e.g., Nginx) to serve static files and proxy to Gunicorn

5. Set up SSL certificate

6. Run Gunicorn:
```bash
gunicorn steelgrid.wsgi:application
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bootstrap for the frontend framework
- Django for the backend framework
- Font Awesome for icons
- AOS for scroll animations 