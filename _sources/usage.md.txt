# ModuFlow Usage Guide

This document provides detailed information on how to use ModuFlow for modular development with TDD.

## Installation

Install ModuFlow from PyPI:

```bash
pip install moduflow
```

## Getting Started

### Initializing a Project

To start using ModuFlow in your project:

```bash
moduflow init
```

This creates:
- `.moduflow/` directory for configuration files
- `design/` directory for module design documents
- Adds necessary entries to `.gitignore`

### Creating Modules

A module is a logical grouping of files that represent a component or feature in your project.

```bash
moduflow create-section users --description "User authentication and management"
```

This creates:
- A configuration file at `.moduflow/config/sections/users.yaml`
- A design file at `design/users.md`

### Adding Files to Modules

You can add files to a module:

```bash
moduflow add-files users users/models.py users/views.py users/tests/test_models.py
```

### Adding a File to Multiple Modules

Some files may be used by multiple modules:

```bash
moduflow add-file .env users,core,api
```

This adds `.env` to the users, core, and api modules.

## Working with Modules

### Listing Modules

To see all modules and their files:

```bash
moduflow list
```

This shows:
- Module names and descriptions
- Files in each module
- Files used by multiple modules

### Analyzing the Project Structure

To get suggestions for modules based on your project structure:

```bash
moduflow analyze
```

This analyzes your directory structure and suggests modules based on directories and Python modules.

## Compilation

ModuFlow can compile modules into isolated directories for testing and development.

### Compiling a Module

To compile a specific module:

```bash
moduflow compile-section users
```

This creates:
- `.compiled_sections/users/` directory
- Copies all files from the users module
- Copies design files for the module
- Creates a manifest file

### Compiling All Modules

To compile all modules separately:

```bash
moduflow compile-all
```

This compiles each module into its own directory under `.compiled_sections/`.

### Compiling the Entire Project

To compile the entire project into a single directory:

```bash
moduflow compile-project
```

This creates:
- `.compiled_sections/project/` directory
- Copies all files from all modules (without duplicates)
- Copies all design files
- Creates a manifest file

## Configuration Management

### Compiling Configuration Files

ModuFlow uses individual YAML files for each module. To compile them into a single configuration file:

```bash
moduflow compile-config
```

This creates:
- `.moduflow/config/compiled.yaml` file

## Working with AI Development

ModuFlow can generate prompts for AI-assisted development.

### Getting the Development Prompt

To generate a development prompt:

```bash
moduflow get-prompt --output prompt.md
```

This creates a Markdown file with:
- Project overview
- Development guidelines
- Module details, including design documents
- Information about files used by multiple modules

## Examples

### Creating a Web Application with Modules

Initialize the project:
```bash
mkdir myapp
cd myapp
moduflow init
```

Create modules:
```bash
moduflow create-section core --description "Core application functionality"
moduflow create-section users --description "User authentication and management"
moduflow create-section api --description "REST API endpoints"
```

Add files to modules:
```bash
moduflow add-files core app.py settings.py
moduflow add-files users users/models.py users/views.py
moduflow add-files api api/endpoints.py api/serializers.py
```

Add shared files:
```bash
moduflow add-file .env core,users,api
moduflow add-file requirements.txt core,users,api
```

Generate AI development prompt:
```bash
moduflow get-prompt --output ai_prompt.md
```

Compile the entire project:
```bash
moduflow compile-project
```

## Advanced Usage

### Using Environment Variables

ModuFlow supports environment variables for customization:

- `MODUFLOW_CONFIG_DIR`: Custom location for the configuration directory
- `MODUFLOW_OUTPUT_DIR`: Custom location for the compiled output
- `MODUFLOW_DESIGN_DIR`: Custom location for design files

### Custom YAML Structure

You can customize the structure of your module YAML files by adding additional fields. These will be preserved when compiled.

For example:
```yaml
name: users
description: User authentication and management
maintainer: surgbc@gmail.com
files:
  - users/models.py
  - users/views.py
dependencies:
  - core
  - database
```

## Troubleshooting

### Common Issues

**Files not being copied during compilation:**
- Make sure the files exist in the project
- Check that the relative paths are correct

**Module configuration not found:**
- Ensure you've initialized the project with `moduflow init`
- Check that the module configuration exists in `.moduflow/config/sections/`

**Changes to module configuration not taking effect:**
- Run `moduflow compile-config` to regenerate the compiled configuration

### Getting Help

For more information:
```bash
moduflow --help
moduflow <command> --help
```