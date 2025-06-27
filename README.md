# Manus Context Manager

A simple, elegant web application for saving and managing project contexts to enable seamless task inheritance.

## Features

- 🧠 **Context Management**: Save and retrieve project contexts with titles, descriptions, and content
- 🎨 **Beautiful Interface**: Modern, responsive web design with gradient backgrounds
- 🚀 **Simple Deployment**: Minimal Flask application optimized for Railway deployment
- 💾 **In-Memory Storage**: Fast, lightweight storage for contexts (resets on restart)
- 🔄 **Real-time Updates**: Instant feedback and dynamic content loading

## API Endpoints

- `GET /` - Main dashboard interface
- `GET /api/contexts` - Retrieve all saved contexts
- `POST /api/contexts` - Save a new context
- `DELETE /api/contexts/<id>` - Delete a specific context
- `GET /health` - Health check endpoint

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open http://localhost:5000 in your browser

## Deployment

This application is optimized for Railway deployment with:
- `Procfile` for process configuration
- `requirements.txt` for dependency management
- Environment variable support for PORT configuration

## Usage

1. **Save Context**: Fill in the title, description, and content fields, then click "Save Context"
2. **View Contexts**: All saved contexts appear in the "Saved Contexts" section
3. **Delete Context**: Click the delete button on any context to remove it

Perfect for maintaining project continuity and enabling seamless task handoffs!

