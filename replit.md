# Overview

Gemini Chat Assistant is a modular Flask web application that provides a chat interface powered by Google's Gemini AI API. The application features a clean, responsive UI with real-time chat functionality, message timestamps, and auto-scrolling. Built with a modular architecture using Flask Blueprints, the project is designed for learning and experimentation with plans for future expansion into specialized tools like ECAD applications and travel dashboards.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Single Page Application**: Uses vanilla JavaScript with Bootstrap 5 for styling and responsiveness
- **Real-time Chat Interface**: Implements asynchronous communication with the backend using fetch API
- **Message Formatting**: Custom CSS styling with monospace fonts, color-coded messages (blue for user, green for Gemini), and timestamps
- **Auto-scroll Functionality**: Automatically scrolls to show latest messages in the chat interface

## Backend Architecture
- **Flask Framework**: Lightweight Python web framework chosen for simplicity and rapid development
- **Blueprint Pattern**: Modular structure using Flask Blueprints to separate chat functionality from main application logic
- **RESTful API Design**: Single POST endpoint `/generate` for handling chat message generation
- **Response Formatting**: Server-side HTML formatting for structured responses including lists and paragraphs

## AI Integration
- **Gemini 1.5 Flash Model**: Selected for fast response times and cost-effectiveness
- **Direct API Integration**: Uses Google's generativeai library for seamless communication with Gemini API
- **Error Handling**: Comprehensive exception handling with user-friendly error messages

## Configuration Management
- **Environment Variables**: Secure API key storage using python-dotenv
- **Flexible Port Configuration**: Supports both local development and cloud deployment through PORT environment variable

# External Dependencies

## Core Technologies
- **Flask**: Web framework for building the application server
- **Google Generative AI**: Official Python client for Gemini API integration
- **Python-dotenv**: Environment variable management for secure configuration

## Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework for responsive design and UI components
- **Bootstrap Icons 1.10.5**: Icon library for enhanced user interface elements

## Cloud Services
- **Google Gemini API**: Primary AI service for natural language processing and response generation
- **Replit Platform**: Hosting and development environment with built-in deployment capabilities

## Development Tools
- **Environment Configuration**: `.env` file support for local API key management
- **Health Check Endpoint**: `/ping` route for monitoring application availability