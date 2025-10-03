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
5. Add authorized redirect URI: `http://localhost:8000/api/v1/auth/callback`
6. Copy Client ID and Client Secret to `.env`

### 4. Run the Application

```bash
python start.py
```

Alternative (manual run):
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

This will start the FastAPI server locally.

### 5. Access the Application

- **Frontend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **API Base**: http://localhost:8000/api/v1
- **Google Login**: http://localhost:8000/api/v1/auth/login

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

### Authentication (versioned)
- `GET /api/v1/auth/login` - Initiate Google OAuth
- `GET /api/v1/auth/callback` - OAuth callback
- `GET /api/v1/auth/me` - Get current user info
- `POST /api/v1/auth/logout` - Logout

### Teachers (versioned)
- `GET /api/v1/teachers/` - List all teachers
- `POST /api/v1/teachers/` - Create new teacher
- `DELETE /api/v1/teachers/{id}` - Delete teacher

### Students (versioned)
- `GET /api/v1/students/` - List all students
- `POST /api/v1/students/` - Create new student
- `DELETE /api/v1/students/{id}` - Delete student

## 🏗️ Project Structure

```
project/
├── app/
│   ├── main.py              # FastAPI application (mounts /api/v1)
│   ├── database.py          # Database configuration
│   ├── api/
│   │   └── v1/
│   │       ├── router.py    # Aggregates v1 routers
│   │       └── routers/
│   │           ├── students.py
│   │           ├── teachers.py
│   │           └── auth.py   # mounts app/auth/router
│   ├── models/              # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── teacher.py
│   │   └── user.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── teacher.py
│   │   └── user.py
│   ├── crud/                # Per-entity data access
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── teacher.py
│   │   └── user.py
│   └── auth/                # Authentication package
│       ├── __init__.py
│       ├── router.py        # /auth/* endpoints
│       └── utils.py         # JWT helpers
├── static/
│   ├── index.html           # Landing page
│   ├── dashboard.html       # Role selection
│   ├── teacher.html         # Teacher dashboard
│   └── student.html         # Student dashboard
├── alembic/                 # Database migrations
├── requirements.txt         # Python dependencies
├── start.py                 # Startup script
└── README.md                # This file
```

## 🧩 Branching & Git Workflow

Use a development branch for feature work and open PRs to main.

```bash
cd project

# initialize repo if needed
git init

# set remote
git remote add origin https://github.com/ahmednoor1006/demo_student_fastapi.git

# create/switch to development
git checkout -B development

# commit and push
git add -A
git commit -m "refactor: v1 API, split modules, auth package"
git push -u origin development
```

Repository: [demo_student_fastapi](https://github.com/ahmednoor1006/demo_student_fastapi.git)

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

