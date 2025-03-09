# Design for core

Core application configuration and settings

## Requirements

The core section is responsible for:

1. Project-wide settings
2. URL routing
3. WSGI/ASGI configuration
4. Middleware setup
5. Static files configuration
6. Template configuration

## Components

### Settings

- Base settings:
  - Installed apps
  - Middleware
  - Templates
  - Databases
  - Static files
  - Media files
  - Auth settings
  - Internationalization

- Development settings:
  - Debug mode enabled
  - Local database
  - Email backend for console

- Production settings:
  - Debug mode disabled
  - Database configuration
  - Proper email backend
  - Security settings
  - Caching configuration

### URLs

- Root URL configuration
- Admin URLs
- API URLs
- Static/Media URLs
- Include URLs from other sections

### WSGI/ASGI

- WSGI application for traditional deployments
- ASGI application for async-capable deployments

## Testing

Tests should cover:

1. Settings configuration
2. URL resolution
3. Middleware functionality
4. Static files serving (in development)

## Implementation Notes

- Use environment variables for sensitive settings
- Use separate settings files for different environments
- Use Django's split settings pattern
- Configure logging properly
- Include proper error handling