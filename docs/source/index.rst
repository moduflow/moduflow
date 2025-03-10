Welcome to ModuFlow's documentation!
====================================

ModuFlow is a command-line tool designed to streamline modular development with built-in support for Test-Driven Development (TDD). It helps developers organize their codebase into logical, independently manageable modules that can be developed, tested, and compiled separately before final integration.

What is ModuFlow?
-----------------

ModuFlow addresses the challenges of maintaining large codebases by dividing them into self-contained modules. It's particularly valuable for AI-assisted development workflows, where context window limitations can make it difficult to work with an entire codebase at once.

Key Benefits
^^^^^^^^^^^^

- **Modular Organization**: Cleanly separate your code into logical components
- **TDD Support**: Facilitate test-driven development for each module
- **AI-Friendly Development**: Generate prompts based on your project structure for AI pair programming
- **Independent Compilation**: Build and test modules in isolation before integration
- **Clear Documentation**: Track which files belong to which modules

Development Workflow
--------------------


ModuFlow supports a structured development approach:

1. Design your system using appropriate diagrams and documentation
2. Divide the system into independent modules that can be developed separately
3. Develop each module using TDD principles, potentially in separate branches
4. Compile and test modules independently
5. Integrate modules into the main branch when complete

This approach is especially powerful when working with AI assistants, as it allows you to focus the context window on specific modules rather than the entire codebase.

Getting Started
---------------


Check out the installation guide and usage examples to begin organizing your projects with ModuFlow.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   overview
   installation
   usage
   modules/index
   development
   testing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`