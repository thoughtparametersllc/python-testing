# python-testing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Python%20Testing-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/python-testing)

GitHub Action to automatically detect and run Python testing frameworks.

## Features

- 🔍 **Automatic Framework Detection** - Automatically detects which testing frameworks your project uses
- 🐍 **Multiple Framework Support** - Supports pytest, unittest, nose2, behave (BDD/Cucumber), tox, and doctest
- 📦 **Custom requirements** - Install additional dependencies from a requirements file
- 📊 **Detailed reporting** - View results in GitHub Actions summary for each detected framework
- 🏷️ **SVG badge generation** - Automatically generate and commit testing badges to your repository
- 📝 **Automatic README updates** - Automatically insert badge references into your README.md
- 🎯 **Framework-specific options** - Pass custom options to each testing framework

## Supported Testing Frameworks

| Framework | Detection Method | Notes |
|-----------|------------------|-------|
| **pytest** | `pytest.ini`, `pyproject.toml`, `setup.cfg`, or `import pytest` in code | Most popular Python testing framework |
| **unittest** | `import unittest` in test files | Built-in Python testing framework |
| **nose2** | `.noserc`, `nose.cfg`, or `[nosetests]` in `setup.cfg` | Successor to nose |
| **behave** | `features/` directory with `.feature` files | BDD/Cucumber-style testing |
| **tox** | `tox.ini` file | Testing across multiple Python environments |
| **doctest** | `>>>` in Python files | Tests embedded in docstrings |

## Usage

> **Note:** Until the first release is tagged, use a specific commit SHA (e.g., `@947908a`) instead of `@v1`. This ensures workflows continue to work even if development branches are deleted. Once v1.0.0 is released, you can use `@v1` for the latest v1.x version.

### Basic Example

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Python Tests
        uses: thoughtparametersllc/python-testing@v1  # or @<commit-sha> before first release
```

### Advanced Example with All Options

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # Required for badge commits
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Python Tests
        uses: thoughtparametersllc/python-testing@v1
        with:
          python-version: '3.11'
          requirements-file: 'requirements.txt'
          pytest-options: '--cov --cov-report=xml'
          unittest-options: '-s tests'
          nose-options: '--verbose'
          behave-options: '--no-capture'
          tox-options: '-e py311'
          generate-badges: 'true'
          badges-directory: '.github/badges'
          update-readme: 'true'
          readme-path: 'README.md'
          badge-style: 'path'
```

### With Badge Generation

Enable badge generation to automatically create SVG badges for each detected framework:

```yaml
- name: Run Python Tests
  uses: thoughtparametersllc/python-testing@v1
  with:
    generate-badges: 'true'
    update-readme: 'true'
    badge-style: 'path'  # or 'url' for GitHub raw URLs
```

When enabled, badges will show passing/failing status for each framework.

**Note:** For badge commits to work, your workflow needs `contents: write` permission:

```yaml
permissions:
  contents: write
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `python-version` | Python version to use for testing | No | `3.x` |
| `requirements-file` | Path to requirements file for additional dependencies | No | `''` |
| `pytest-options` | Additional options to pass to pytest | No | `''` |
| `unittest-options` | Additional options to pass to unittest | No | `''` |
| `nose-options` | Additional options to pass to nose2 | No | `''` |
| `behave-options` | Additional options to pass to behave | No | `''` |
| `tox-options` | Additional options to pass to tox | No | `''` |
| `generate-badges` | Generate and commit SVG badges to the repository | No | `false` |
| `badges-directory` | Directory where badge SVG files will be saved | No | `.github/badges` |
| `update-readme` | Automatically update README.md with badge references | No | `false` |
| `readme-path` | Path to README.md file to update with badges | No | `README.md` |
| `badge-style` | Badge style: 'url' for GitHub URLs or 'path' for relative paths | No | `path` |

## How Framework Detection Works

The action intelligently detects which testing frameworks are used in your project:

1. **pytest**: Looks for `pytest.ini`, `pyproject.toml`, `setup.cfg`, or `import pytest` statements
2. **unittest**: Searches for `import unittest` in test files
3. **nose2**: Checks for `.noserc`, `nose.cfg`, or nose configuration in `setup.cfg`
4. **behave**: Detects `features/` directory containing `.feature` files
5. **tox**: Looks for `tox.ini` configuration file
6. **doctest**: Searches for `>>>` patterns indicating docstring tests

Only detected frameworks will be installed and run.

## Examples

### pytest Project

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov=mypackage --cov-report=xml'
```

### Multiple Frameworks

The action will automatically run all detected frameworks:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    requirements-file: 'requirements-dev.txt'
    pytest-options: '--verbose'
    behave-options: '--tags=@smoke'
```

### BDD with Behave

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    behave-options: '--format=progress --tags=@automated'
    generate-badges: 'true'
```

## Badge Display

When `update-readme` is enabled, badges are automatically inserted after your README title:

```markdown
# My Project

<!-- testing-badges-start -->
![Pytest](.github/badges/pytest.svg)
![Unittest](.github/badges/unittest.svg)
<!-- testing-badges-end -->
```

Manual badge references (if not using `update-readme`):

```markdown
![Pytest](.github/badges/pytest.svg)
![Unittest](.github/badges/unittest.svg)
![Nose2](.github/badges/nose2.svg)
![Behave](.github/badges/behave.svg)
![Tox](.github/badges/tox.svg)
![Doctest](.github/badges/doctest.svg)
```

## Roadmap

Future enhancements planned:

- **Automated versioning and tagging** - Semantic versioning with automated tag creation
- **GitHub Marketplace publishing** - Automated publishing workflow for releases
- **Additional frameworks** - Support for robotframework, green, testify, Ward
- **Enhanced reporting** - Code coverage integration, test timing analysis
- **Performance optimization** - Parallel test execution, dependency caching

## Development

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

### Testing Locally

You can test the action locally by creating a test workflow in your repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Actions

- [python-linting](https://github.com/thoughtparametersllc/python-linting) - Companion action for Python linting with pylint, black, and mypy

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/thoughtparametersllc/python-testing/issues) on GitHub.
