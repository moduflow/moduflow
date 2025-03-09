#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Install dependencies
pip install -r requirements.txt

# Clean up previous build artifacts
rm -rf dist build *.egg-info

# Determine which Python executable to use
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "Error: Python executable not found"
    exit 1
fi

echo "Using Python: $($PYTHON --version)"

# Run the version checker to get package name and update versions
python_package_name=$($PYTHON versionChecker.py)
if [ -z "$python_package_name" ]; then
    echo "Error: Failed to get package name from versionChecker.py"
    exit 1
fi

echo "Package name: $python_package_name"

# Build the distribution
echo "Building package distribution..."
$PYTHON -m build

# Check if files were created
if [ ! -d "dist" ] || [ -z "$(ls -A dist)" ]; then
    echo "Error: Build failed, no distribution files created"
    exit 1
fi

echo "Distribution files created:"
ls -la dist/

# Upload to PyPI
echo "Uploading to PyPI..."
$PYTHON -m twine upload dist/* --verbose

echo "Build and upload completed successfully"