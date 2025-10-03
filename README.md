# 🎓 Student Teacher Management System

A modern web application for managing students and teachers with Google OAuth authentication.

## ✨ Features

- 🔐 **Google OAuth Authentication** - Secure login with Google accounts
- 👨‍🏫 **Teacher Dashboard** - Manage students, assign marks, track progress
- 👨‍🎓 **Student Dashboard** - View academic performance and statistics
- 📊 **Analytics** - Performance tracking and grade analytics
- 🎨 **Modern UI** - Beautiful, responsive design
- 🔒 **Secure API** - JWT-based authentication for all endpoints

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- Google OAuth credentials

### 1. Setup Database

Create a PostgreSQL database:
```sql
CREATE DATABASE student_db;
```

### 2. Configure Environment

Copy the example environment file:
```bash
cp env_example .env
```

Update `.env` with your values:
```env
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=student_db

SECRET_KEY=your-super-secret-key-change-this-in-production
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 3. Get Google OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URI: `http://localhost:8000/auth/callback`
6. Copy Client ID and Client Secret to `.env`

### 4. Run the Application

```bash
python start.py
```

This will:
- Install requirements
- Setup environment
- Run database migrations
- Start the FastAPI server

### 5. Access the Application

- **Frontend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Google Login**: http://localhost:8000/auth/login

## 📱 Usage

### Authentication Flow

1. Visit http://localhost:8000
2. Click "Login with Google"
3. Authorize with your Google account
4. Choose Teacher or Student dashboard

### Teacher Dashboard

- ➕ Add new teachers and students
- 📊 View all students and their marks
- 🗑️ Delete teachers and students
- 📈 Track class performance

### Student Dashboard

- 📚 View all student records
- 📊 See performance statistics
- 👨‍🏫 View teacher information
- 🏆 Track top performers

## 🛠️ API Endpoints

### Authentication
- `GET /auth/login` - Initiate Google OAuth
- `GET /auth/callback` - OAuth callback
- `GET /auth/me` - Get current user info
- `POST /auth/logout` - Logout

### Teachers
- `GET /teachers/` - List all teachers
- `POST /teachers/` - Create new teacher
- `DELETE /teachers/{id}` - Delete teacher

### Students
- `GET /students/` - List all students
- `POST /students/` - Create new student
- `DELETE /students/{id}` - Delete student

## 🏗️ Project Structure

```
project/
├── app/
│   ├── main.py          # FastAPI application
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database configuration
│   ├── auth.py          # Authentication routes
│   ├── auth_utils.py    # JWT utilities
│   └── crud.py          # Database operations
├── static/
│   ├── index.html       # Landing page
│   ├── dashboard.html   # Role selection
│   ├── teacher.html     # Teacher dashboard
│   └── student.html     # Student dashboard
├── alembic/             # Database migrations
├── requirements.txt     # Python dependencies
├── start.py            # Startup script
└── README.md           # This file
```

## 🔧 Development

### Manual Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
alembic upgrade head
```

4. Start development server:
```bash
cd app
uvicorn main:app --reload
```

### Database Migrations

Create new migration:
```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
alembic upgrade head
```

## 🎨 Frontend Features

- **Responsive Design** - Works on desktop and mobile
- **Modern UI** - Clean, professional interface
- **Real-time Updates** - Dynamic data loading
- **Error Handling** - User-friendly error messages
- **Progress Bars** - Visual performance indicators
- **Grade Badges** - Color-coded grade display

## 🔒 Security Features

- **JWT Authentication** - Secure token-based auth
- **Google OAuth** - Trusted authentication provider
- **Session Management** - Secure session handling
- **Input Validation** - Pydantic schema validation
- **SQL Injection Protection** - SQLAlchemy ORM

## 📊 Database Schema

### Users Table
- `id` - Primary key
- `email` - Unique email from Google
- `name` - User's display name

### Teachers Table
- `id` - Primary key
- `name` - Teacher's name
- `subject` - Subject taught

### Students Table
- `id` - Primary key
- `name` - Student's name
- `marks` - Academic marks (0-100)
- `teacher_id` - Foreign key to teachers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**Database Connection Error**
- Ensure PostgreSQL is running
- Check database credentials in `.env`
- Verify database exists

**Google OAuth Error**
- Check Client ID and Secret in `.env`
- Verify redirect URI in Google Console
- Ensure Google+ API is enabled

**Static Files Not Loading**
- Check file paths in `main.py`
- Ensure `static/` directory exists
- Verify file permissions

### Support

For issues and questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Check server logs for errors

## 🎯 Future Enhancements

- 📧 Email notifications
- 📱 Mobile app
- 📈 Advanced analytics
- 🎓 Grade management
- 📅 Assignment scheduling
- 💬 Messaging system

