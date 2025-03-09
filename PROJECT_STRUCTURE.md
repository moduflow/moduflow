# ModuFlow Project Structure

This document outlines the structure of the ModuFlow project, designed to support modular development with branch-based workflow.

## Directory Structure

```
moduflow/
├── pyproject.toml               # Project metadata and dependencies
├── setup.py                     # Setup script for installation 
├── setup.cfg                    # Configuration for setup
├── requirements.txt             # Project dependencies
├── pytest.ini                   # Configuration for pytest
├── versionChecker.py            # Script to extract package version
├── build.sh                     # Build and publish script
├── README.md                    # Main documentation
├── LICENSE                      # Project license
├── .gitignore                   # Git ignore file
├── .github/                     # GitHub specific files
│   └── workflows/               # GitHub Actions workflows
│       └── publish.yml          # Workflow to publish package to PyPI
├── moduflow/                    # Main package directory
│   ├── __init__.py              # Package initialization
│   ├── __main__.py              # Entry point for running as module
│   ├── cli/                     # CLI module
│   │   ├── __init__.py          # CLI package initialization
│   │   ├── main.py              # CLI entry point
│   │   └── commands.py          # CLI commands implementation
│   ├── core/                    # Core functionality module
│   │   ├── __init__.py          # Core package initialization 
│   │   ├── config.py            # Configuration handling
│   │   ├── paths.py             # Path management
│   │   └── exceptions.py        # Custom exceptions
│   ├── handlers/                # File and operations handlers module
│   │   ├── __init__.py          # Handlers package initialization
│   │   ├── yaml_handler.py      # YAML file handling
│   │   ├── file_handler.py      # File operations
│   │   └── section_handler.py   # Module management
│   ├── compilers/               # Compilation module
│   │   ├── __init__.py          # Compilers package initialization
│   │   ├── section.py           # Module compilation
│   │   └── project.py           # Project compilation
│   ├── prompts/                 # AI prompts module
│   │   ├── __init__.py          # Prompts package initialization
│   │   └── templates.py         # Prompt templates
│   └── utils/                   # Utilities module
│       ├── __init__.py          # Utils package initialization
│       └── helpers.py           # Helper functions
├── tests/                       # Test directory
│   ├── __init__.py              # Test package initialization
│   ├── test_cli.py              # CLI tests
│   ├── test_core.py             # Core functionality tests
│   ├── test_handlers.py         # Handlers tests
│   ├── test_compilers.py        # Compilers tests
│   └── test_utils.py            # Utils tests
└── docs/                        # Documentation directory
    ├── usage.md                 # Usage documentation
    ├── development.md           # Development documentation
    └── examples/                # Example files
        ├── simple_project/      # Simple project example
        └── advanced_project/    # Advanced project example
```

## Branch Strategy

The project uses a branch-based development workflow:

1. `master` - Main stable branch
2. `cli` - Branch for CLI development
3. `core` - Branch for core functionality
4. `handlers` - Branch for file and module handlers
5. `compilers` - Branch for compilation functionality
6. `prompts` - Branch for AI prompt generation

Each module should be developed in its respective branch, with tests, and then merged into `master` when ready.

## Installation for Development

To install the package for development:

```bash
git clone https://github.com/moduflow/moduflow.git
cd moduflow
pip install -e .
```

## Running Tests

To run the tests:

```bash
pytest
```

Or to run tests with coverage:

```bash
pytest --cov=moduflow
```

## Configuration Structure

ModuFlow uses YAML for configuration, with separate files for each module:

```
.moduflow/                 # Hidden directory for configuration files
├── config/                # Configuration directory
│   ├── sections/          # Individual module configurations
│   │   ├── users.yaml     # Users module config
│   │   ├── core.yaml      # Core module config
│   │   └── ...            # Other module configs
│   └── compiled.yaml      # Compiled configuration (generated)
```