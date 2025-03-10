# Overview

ModuFlow is a command-line tool designed to facilitate modular development with a focus on AI-assisted workflows. This document provides an in-depth overview of ModuFlow's core concepts, workflow, and how it integrates with AI-driven development.

## The Problem ModuFlow Solves

When working with AI assistants to develop software:

1. **Context Window Limitations**: AI models have limited context windows, making it difficult to work with entire codebases at once
2. **Project Organization**: Maintaining clear boundaries between components becomes challenging as projects grow
3. **Development Continuity**: Tracking progress across multiple AI sessions requires structured approaches

ModuFlow addresses these challenges by providing a structured way to divide your project into manageable modules that can be developed independently.

## Design-First Approach

ModuFlow encourages a design-first approach, where system architecture is defined before implementation begins. The design files (stored in the `design/` directory) can include:

### Sequence Diagrams

```
┌─────┐          ┌─────────┐          ┌───────────┐
│User │          │AuthModule│          │UserService│
└──┬──┘          └────┬────┘          └─────┬─────┘
   │    login()       │                     │
   │ ───────────────> │                     │
   │                  │   validateUser()    │
   │                  │ ──────────────────> │
   │                  │                     │
   │                  │ ◀─────────────────  │
   │                  │    user object      │
   │ ◀───────────────┐│                     │
   │   auth token     │                     │
┌──┴──┐          ┌────┴────┐          ┌─────┴─────┐
│User │          │AuthModule│          │UserService│
└─────┘          └─────────┘          └───────────┘
```

### Class Diagrams

```
┌───────────────────┐      ┌────────────────────┐
│ User               │      │ AuthService        │
├───────────────────┤      ├────────────────────┤
│ - id: UUID         │      │ - tokenStore: Dict │
│ - username: String │      ├────────────────────┤
│ - email: String    │◄─────│ + login()          │
│ - passwordHash: Str│      │ + logout()         │
├───────────────────┤      │ + register()        │
│ + validatePwd()    │      │ + resetPassword()  │
└───────────────────┘      └────────────────────┘
```

## AI-Driven Module Definition

One of ModuFlow's key features is facilitating AI-driven project structuring. After sharing your design with an AI assistant, you can ask it to suggest a modular structure for your project.

The AI will analyze your requirements and design to produce module definitions like:

```yaml
name: users
description: User authentication, registration, and profile management
files:
  - users/__init__.py
  - users/models.py
  - users/views.py
  - users/forms.py
  - users/serializers.py
  - users/settings.py
  - users/tests/__init__.py
  - users/tests/test_models.py
  - users/tests/test_views.py
  - users/README.md
  - .env
  - requirements.txt
  - docker-compose.yml
  - Dockerfile
  - common/__init__.py
  - common/utils.py
  - common/mixins.py
  - static/css/main.css
  - static/js/app.js
  - templates/base.html
```

These module definitions can then be imported into ModuFlow using:

```bash
moduflow import-section users.yaml
```

## Development Workflow

With ModuFlow, your development workflow becomes:

1. **Design**: Create system diagrams and architecture documents
2. **Module Definition**: Have an AI assistant suggest module breakdown based on your design
3. **Module Creation**: Import the AI-suggested modules into ModuFlow
4. **Implementation**: Develop each module separately, often in dedicated branches
5. **Testing**: Use TDD to ensure each module works correctly in isolation
6. **Integration**: Compile all modules together and test the integrated system

## Module-Focused AI Development

When working with an AI assistant on a specific module, you can generate a focused prompt:

```bash
moduflow get-prompt users --output users_prompt.md
```

This produces a prompt containing:
- The module description and file structure
- Design documents relevant to this module
- Test requirements for the module
- Dependencies on other modules

You can then share this prompt with an AI assistant to receive more focused and accurate code generation.

## Module Independence and Integration

ModuFlow helps maintain the balance between module independence and system integration:

- **Independent Development**: Each module can be developed and tested separately
- **Shared Resources**: Common files can be assigned to multiple modules
- **Compilation**: Modules can be compiled individually or together
- **Dependency Management**: ModuFlow tracks inter-module dependencies

This approach ensures that modules can be developed in parallel while still maintaining a cohesive system architecture.