# Flask REST API

A modern Flask REST API with SQLAlchemy ORM, featuring a companies endpoint with full CRUD operations.

## 🚀 Features

- **Flask 3.x** with modern Python support
- **SQLAlchemy ORM** for database operations
- **SQLite** database (configurable for PostgreSQL/MySQL)
- **RESTful API** design with JSON responses
- **Blueprint-based** architecture
- **CRUD operations** for companies
- **Query parameters** for filtering and pagination
- **Error handling** with proper HTTP status codes

## 📋 Requirements

- Python 3.9+
- Flask 3.1.1
- Flask-SQLAlchemy 3.1.1
- SQLAlchemy-Utils 0.41.2

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd flask-rest-api
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Initialize the database:**
   ```bash
   python3 init_db.py
   ```

4. **Run the application:**
   ```bash
   python3 run.py
   ```

The API will be available at `http://localhost:5000`

## 🗄️ Database Setup

The application uses SQLite by default. To initialize the database tables:

```bash
# Option 1: Use the init-db endpoint
curl http://localhost:5000/init-db

# Option 2: Run the init script
python3 init_db.py
```

## 📚 API Endpoints

### Home
- **GET** `/` - Returns API information

### Companies

#### List Companies
- **GET** `/companies/` - Get all companies
  - Query parameters:
    - `name` (optional): Filter by company name
    - `order_by` (optional): Sort by field (name, id, country_code)
    - `offset` (optional): Pagination offset (default: 0)
    - `limit` (optional): Pagination limit (default: 10)

#### Get Company
- **GET** `/companies/{id}` - Get a specific company by ID

#### Create Company
- **POST** `/companies/` - Create a new company
  ```json
  {
    "name": "Example Corp",
    "country_code": "US",
    "website": "https://example.com",
    "enabled": true
  }
  ```

#### Update Company
- **POST/PATCH** `/companies/{id}` - Update an existing company
  ```json
  {
    "name": "Updated Corp",
    "country_code": "CA",
    "website": "https://updated.com",
    "enabled": false
  }
  ```

#### Delete Company
- **DELETE** `/companies/{id}` - Delete a company

## 🏗️ Project Structure

```
flask-rest-api/
├── flask_rest_app/
│   ├── __init__.py          # Flask extensions
│   ├── application.py       # App factory
│   ├── config.py           # Configuration classes
│   └── companies/
│       ├── __init__.py
│       ├── models.py       # SQLAlchemy models
│       ├── schemas.py      # Data serialization
│       └── views.py        # API endpoints
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
├── run.py                 # Application runner
├── init_db.py             # Database initialization
└── README.md              # This file
```

## 🧪 Testing

Run the tests:
```bash
python3 -m pytest tests/
```

## 🔧 Configuration

The application supports different environments:

- **Development**: `APP_ENV=development` (default)
- **Testing**: `APP_ENV=testing`
- **Production**: `APP_ENV=production`

Database URLs can be configured in `flask_rest_app/config.py`.

## 🚀 Deployment

For production deployment:

1. Set `APP_ENV=production`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure a production database (PostgreSQL, MySQL)
4. Set up proper environment variables

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.
