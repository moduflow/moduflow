# ModuFlow Development Guide

This document provides information for developers who want to contribute to ModuFlow.

## Project Structure

```
moduflow/
├── moduflow/                # Main package directory
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point for running as module
│   ├── cli/                 # CLI section
│   │   ├── __init__.py      # CLI package initialization
│   │   ├── main.py          # CLI entry point
│   │   └── commands.py      # CLI commands implementation
│   ├── core/                # Core functionality section
│   │   ├── __init__.py      # Core package initialization 
│   │   ├── config.py        # Configuration handling
│   │   ├── paths.py         # Path management
│   │   └── exceptions.py    # Custom exceptions
│   ├── handlers/            # File and operations handlers section
│   │   ├── __init__.py      # Handlers package initialization
│   │   ├── yaml_handler.py  # YAML file handling
│   │   ├── file_handler.py  # File operations
│   │   └── section_handler.py # Section management
│   ├── compilers/           # Compilation section
│   │   ├── __init__.py      # Compilers package initialization
│   │   ├── section.py       # Section compilation
│   │   └── project.py       # Project compilation
│   ├── prompts/             # AI prompts section
│   │   ├── __init__.py      # Prompts package initialization
│   │   └── templates.py     # Prompt templates
│   └── utils/               # Utilities section
│       ├── __init__.py      # Utils package initialization
│       └── helpers.py       # Helper functions
├── tests/                   # Test directory
├── docs/                    # Documentation directory
└── ...                      # Other project files
```

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/moduflow/moduflow.git
   cd moduflow
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Branch Strategy

The project uses a branch-based development workflow:

1. `master` - Main stable branch
2. `cli` - Branch for CLI development
3. `core` - Branch for core functionality
4. `handlers` - Branch for file and section handlers
5. `compilers` - Branch for compilation functionality
6. `prompts` - Branch for AI prompt generation

When working on a feature:

1. Create a branch from `master` or the appropriate section branch
2. Implement and test your changes
3. Create a pull request targeting the appropriate section branch
4. After review, the section branch will be merged into `master`

## Testing

Run the tests with pytest:

```bash
pytest
```

Add new tests in the `tests/` directory, following the same structure as the main package.

## Code Style

This project follows PEP 8 style guidelines with a few exceptions. We use:

- Black for code formatting
- isort for import sorting
- flake8 for linting

You can run these tools with:

```bash
black moduflow tests
isort moduflow tests
flake8 moduflow tests
```

## Documentation

Documentation is written in Markdown and stored in the `docs/` directory. 

To build the documentation:

```bash
cd docs
mkdocs build
```

To serve the documentation locally:

```bash
cd docs
mkdocs serve
```

## Release Process

1. Update version in:
   - `pyproject.toml`
   - `setup.cfg`
   - `moduflow/__init__.py`

2. Update the CHANGELOG.md

3. Create a release commit:
   ```bash
   git commit -am "Release vX.Y.Z"
   ```

4. Tag the release:
   ```bash
   git tag vX.Y.Z
   ```

5. Push to GitHub:
   ```bash
   git push origin master --tags
   ```

6. Build and upload to PyPI:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

## Adding New Commands

1. Create a new command function in `moduflow/cli/commands.py`
2. Add the command to the CLI group in `moduflow/cli/main.py`
3. Add tests for the command in `tests/test_cli.py`
4. Update the documentation in `docs/usage.md`

## Working with Sections

Sections are the core concept of ModuFlow. When adding functionality related to sections:

1. Consider which component it belongs to (core, handlers, compilers, etc.)
2. Add appropriate tests
3. Update documentation

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Please make sure your code passes all tests and follows the style guidelines.
