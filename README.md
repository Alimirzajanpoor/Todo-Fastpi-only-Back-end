# Todo-FastAPI-only-Back-end

This is a backend project for a Todo app built using the FastAPI framework in Python. The project provides endpoints for creating, reading, updating, and deleting todo items in a database. It uses Celery and RabbitMQ for background task processing, SQLAlchemy as the ORM, PostgreSQL as the database management system, Docker for containerization, and the requests module for sending todos to the client and to a Telegram bot.

## Installation
To run the project, you'll need to have the following technologies installed on your machine:

- Python 3.x
- Docker
- RabbitMQ
- Celery
- PostgresSQL
- SQLAlchemy

Next, you'll need to install the project dependencies. To do this, navigate to the project directory in your terminal and run the following command
-'pip install -r requirements.txt'
this will install all the required Python dependencies for the project.

### Environment Variables
You also need to create a single `.env` file and specify the below required environment variables:
- 'SQLALCHAMY_DATABASE_URL'
- 'POSTGRES_USER'
- 'POSTGRES_PASSWORD'
- 'POSTGRES_DB'
- 'TOKEN_TEL'
- 'SECRET_KEY'
- 'ALGORITHM'
- 'ACCESS_TOKEN_EXPIRE_MINUTES'
- 'RABBITMQ_URL'

## Usage

### Running the project with Docker

To start the server, RabbitMQ, and PostgreSQL with Docker, run the following command from the project directory:
- 'docker-compose up --build'
### Running the project without Docker

first you need to install RabbitMQ,and PostgresSQL and installing requirements.txt:

start the Celery worker, open a new terminal window and navigate to the project directory. Run the following command:

-`celery -A tasks worker --loglevel=info`

run `uvicorn main:app`



