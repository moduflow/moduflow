#!/usr/bin/env python3
"""
Version checker script for ModuFlow.

This script checks the current version in PyPI and local files and determines
the appropriate version number for the new release.
"""

import os
import re
import json
import subprocess
import sys
from typing import Tuple, Optional


def get_local_version() -> str:
    """Extract version from the package's __init__.py file."""
    try:
        init_file = "moduflow/__init__.py"
        
        with open(init_file, "r") as f:
            content = f.read()
        
        version_match = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content)
        if version_match:
            return version_match.group(1)
        return "0.1.0"  # Default version if not found
    except Exception as e:
        print(f"Error extracting local version: {e}", file=sys.stderr)
        return "0.1.0"


def get_pypi_version(package_name: str) -> Optional[str]:
    """Get the latest version of the package from PyPI."""
    try:
        # Try using pip to get package info
        result = subprocess.run(
            ["pip", "index", "versions", package_name],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            # Parse the output
            output = result.stdout
            version_match = re.search(r'Available versions: ([\d\.]+)', output)
            if version_match:
                return version_match.group(1)
            
        # Alternative method using PyPI API
        try:
            import requests
            response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
            if response.status_code == 200:
                data = response.json()
                return data["info"]["version"]
        except (ImportError, Exception):
            pass
            
        return None  # Package not found or error
    except Exception as e:
        print(f"Error checking PyPI version: {e}", file=sys.stderr)
        return None


def increment_version(version: str) -> str:
    """Increment the patch version number."""
    major, minor, patch = version.split(".")
    new_patch = int(patch) + 1
    return f"{major}.{minor}.{new_patch}"


def update_version_files(new_version: str) -> None:
    """Update version in all necessary files."""
    # Update in __init__.py
    init_file = "moduflow/__init__.py"
    try:
        with open(init_file, "r") as f:
            content = f.read()
        
        new_content = re.sub(
            r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f'__version__ = "{new_version}"',
            content
        )
        
        with open(init_file, "w") as f:
            f.write(new_content)
        
        # Update in pyproject.toml
        with open("pyproject.toml", "r") as f:
            content = f.read()
        
        new_content = re.sub(
            r'version\s*=\s*[\'"]([^\'"]*)[\'"]',
            f'version = "{new_version}"',
            content
        )
        
        with open("pyproject.toml", "w") as f:
            f.write(new_content)
            
        # Update in setup.cfg
        with open("setup.cfg", "r") as f:
            content = f.read()
        
        new_content = re.sub(
            r'version\s*=\s*([\d\.]+)',
            f'version = {new_version}',
            content
        )
        
        with open("setup.cfg", "w") as f:
            f.write(new_content)
            
        print(f"Version updated to {new_version} in all files", file=sys.stderr)
    except Exception as e:
        print(f"Error updating version files: {e}", file=sys.stderr)


def determine_version() -> Tuple[str, str]:
    """
    Determine the package name and version to use.
    
    Returns:
        Tuple of (package_name, version)
    """
    package_name = "moduflow"
    
    # Get current local version
    local_version = get_local_version()
    
    # Get PyPI version if available
    pypi_version = get_pypi_version(package_name)
    
    if pypi_version:
        # If PyPI version exists, compare with local version
        local_parts = [int(x) for x in local_version.split('.')]
        pypi_parts = [int(x) for x in pypi_version.split('.')]
        
        # Compare versions
        if local_parts > pypi_parts:
            # Local version is higher than PyPI, use local version
            new_version = local_version
            print(f"Local version {local_version} is higher than PyPI version {pypi_version}. Using local version.", file=sys.stderr)
        else:
            # PyPI version is same or higher, increment PyPI version
            new_version = increment_version(pypi_version)
            print(f"Incrementing PyPI version {pypi_version} to {new_version}", file=sys.stderr)
    else:
        # No PyPI version found, use local version
        new_version = local_version
        print(f"No PyPI version found. Using local version {local_version}", file=sys.stderr)
    
    # Update version in all files
    update_version_files(new_version)
    
    return package_name, new_version


if __name__ == "__main__":
    package_name, version = determine_version()
    # Print only the package name to stdout (used by build.sh)
    print(package_name, end="")