# Testing ModuFlow

This document provides information on how to run and write tests for the ModuFlow project.

## Running Tests

ModuFlow uses pytest for testing. You can run the tests with:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run tests with coverage report
pytest --cov=moduflow

# Run tests in a specific file
pytest tests/test_core.py

# Run a specific test
pytest tests/test_core.py::TestConfigManager::test_init_config
```

## Test Structure

Tests are organized in the `tests/` directory, mirroring the main package structure:

- `test_cli.py` - Tests for CLI functionality
- `test_core.py` - Tests for core functionality
- `test_handlers.py` - Tests for handlers
- `test_compilers.py` - Tests for compilers
- `test_utils.py` - Tests for utilities

## Writing Tests

When adding new features, please add corresponding tests. Tests should:

1. Test each function's main functionality
2. Include tests for edge cases and error handling
3. Use proper setup and teardown
4. Be isolated from each other (no dependencies between tests)

### Example Test Structure

```python
import unittest
from moduflow.core.config import ConfigManager

class TestConfigManager(unittest.TestCase):
    """Tests for ConfigManager."""
    
    def setUp(self):
        """Set up test environment."""
        # Create test resources
        pass
    
    def tearDown(self):
        """Clean up test environment."""
        # Clean up test resources
        pass
    
    def test_some_functionality(self):
        """Test description here."""
        # Arrange
        manager = ConfigManager()
        
        # Act
        result = manager.some_method()
        
        # Assert
        self.assertEqual(result, expected_value)
```

## Integration with CI/CD

Tests are automatically run in GitHub Actions:

1. Tests run on every push to any branch
2. Tests run when a pull request is opened/updated
3. Tests must pass before a pull request can be merged
4. Tests run on multiple Python versions (3.7, 3.8, 3.9, 3.10)

## Adding More Tests

Currently, the basic tests are set up for the core functionality. As you develop other modules, please add tests for:

1. **CLI Commands** - Test each command with various inputs
2. **Handlers** - Test file, YAML, and section handling
3. **Compilers** - Test compilation of sections and projects
4. **Prompts** - Test generation of prompts
5. **Utils** - Test utility functions

## Test Coverage

Aim for at least 80% test coverage for all modules. You can check coverage with:

```bash
pytest --cov=moduflow --cov-report=term-missing
```