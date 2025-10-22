✨ To-Do Web App: Flask + MySQL + Docker Compose
🚀 Quick Start (Up in 60 Seconds)
This project provides a simple, persistent To-Do list application built with Flask (Python) and backed by a MySQL database, all containerized with Docker Compose. It ensures a consistent development environment for everyone!
Prerequisites
Make sure you have Docker Desktop (which includes Docker Engine and Docker Compose) installed and running.

1. Run the Stack
Navigate to the project's root directory (where docker-compose.yaml is located) and execute the following command:
docker compose up --build -d

2. Access the App
Once the containers are running, open your web browser and go to:

👉 http://localhost:5008
Component               Role                Version/Tech
Frontend/Backend     Web Application         Flask (Python)
Database             Persistence/Storage     MySQL 8.0
Orchestration        Setup & Networking      Docker Compose
Containerization     Packaging               Dockerfile (Python 3.9-slim)

📁 Project Structure
├── app/
│   ├── app.py              # Flask routes and MySQL connection logic.
│   ├── requirements.txt    # Lists Flask and mysql-connector-python.
│   └── templates/
│       └── index.html      # Simple HTML/Jinja2 UI.
├── docker-compose.yaml     # Defines and links 'web' and 'db' services.
├── Dockerfile              # Instructions for building the Flask application container.
└── README.md

🌐 Networking & Data Persistence
Port MappingWeb App: 
Host Port 5008 --> Container Port 5000 (Defined in docker-compose.yaml).Database Host: The Flask app connects to the database using the service name db (not localhost).

Data
The MySQL data is saved outside the container using a Docker named volume (db_data). This means your to-do list items will persist even if you stop and restart the containers.

🛑 Management Commands
Use these commands from the project root:
Command                              Description
docker compose up -d                 Start all services (after the initial build).
docker compose down                  Stop and remove containers and network.
docker compose logs -f               View real-time logs for all services (useful for debugging).
docker exec -it todo-db bash         Open a Bash shell inside the MySQL container.

