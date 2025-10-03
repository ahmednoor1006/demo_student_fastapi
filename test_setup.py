#!/usr/bin/env python3
"""
Test script to verify the setup is working correctly
"""
import os
import sys
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import fastapi
        print("✅ FastAPI")
        
        import uvicorn
        print("✅ Uvicorn")
        
        import sqlalchemy
        print("✅ SQLAlchemy")
        
        import psycopg2
        print("✅ Psycopg2")
        
        import alembic
        print("✅ Alembic")
        
        import pydantic
        print("✅ Pydantic")
        
        from dotenv import load_dotenv
        print("✅ Python-dotenv")
        
        from jose import jwt
        print("✅ Python-jose")
        
        from authlib.integrations.starlette_client import OAuth
        print("✅ Authlib")
        
        import httpx
        print("✅ HTTPX")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_app_structure():
    """Test if the application structure is correct"""
    print("\n📁 Testing application structure...")
    
    required_files = [
        "app/main.py",
        "app/models.py", 
        "app/schemas.py",
        "app/database.py",
        "app/auth.py",
        "app/auth_utils.py",
        "app/crud.py",
        "static/index.html",
        "static/dashboard.html",
        "static/teacher.html",
        "static/student.html",
        "requirements.txt",
        "alembic.ini"
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - Missing")
            all_exist = False
    
    return all_exist

def test_env_setup():
    """Test environment setup"""
    print("\n🔧 Testing environment setup...")
    
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file exists")
        
        from dotenv import load_dotenv
        load_dotenv()
        
        required_vars = [
            "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME",
            "SECRET_KEY", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"
        ]
        
        all_set = True
        for var in required_vars:
            value = os.getenv(var)
            if value and value != f"your-{var.lower().replace('_', '-')}":
                print(f"✅ {var}")
            else:
                print(f"⚠️  {var} - Not configured")
                all_set = False
        
        return all_set
    else:
        print("❌ .env file not found")
        return False

def test_app_import():
    """Test if the FastAPI app can be imported"""
    print("\n🚀 Testing FastAPI app import...")
    
    try:
        sys.path.insert(0, 'app')
        from main import app
        print("✅ FastAPI app imported successfully")
        print(f"✅ App title: {app.title}")
        return True
    except Exception as e:
        print(f"❌ Failed to import app: {e}")
        return False

def main():
    """Run all tests"""
    print("🎓 Student Teacher Management System - Setup Test")
    print("=" * 60)
    
    tests = [
        ("Package Imports", test_imports),
        ("Application Structure", test_app_structure), 
        ("Environment Setup", test_env_setup),
        ("FastAPI App", test_app_import)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}")
        print("-" * len(test_name))
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<25} {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! Your setup is ready.")
        print("🚀 Run 'python start.py' to start the application")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("📖 Check README.md for setup instructions")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
