# ACME Inc Python Web Application

A simple Flask web server that replaces the original Node.js application.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The server will start on port 3000 by default.

## Endpoints

- `/` - Welcome message with service information
- `/health` - Health check endpoint
- `/api/info` - Application information and status

## Environment Variables

- `PORT` - Port to run the server on (default: 3000)
- `FLASK_ENV` - Environment mode (default: development)
