# Chat Server App

A real-time chat application built with Python and Django.  
Supports live messaging and user authentication.

---

## Features

- Real-time chat using WebSockets
- Public chat room
- User authentication
---

## Tech Stack

- Python
- Django 
- Redis (channel layer backend)
- Daphne (ASGI server)

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

    Install dependencies:

pip install -r requirements.txt

    Apply database migrations:

python manage.py migrate

    Create a superuser (optional):

python manage.py createsuperuser

    Start Redis server (make sure Redis is installed and running on localhost:6379):

redis-server

    Run the development server:

python manage.py runserver

    Navigate to: 127.0.0.1:8000/login

Once you login you will be in the chat
