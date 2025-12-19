# python-testing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Python%20Testing-blue.svg?colorA=24292e&colorB=0366d6&style=flat&longCache=true&logo=github)](https://github.com/marketplace/actions/python-testing)

GitHub Action to run Python tests using pytest.

## Features

- 🐍 **pytest Testing** - Run pytest tests with configurable options
- 📦 **Custom requirements** - Install additional dependencies from a requirements file
- 📊 **Detailed reporting** - View test results in GitHub Actions summary
- 🏷️ **SVG badge generation** - Automatically generate and commit testing badges to your repository
- 🎯 **Framework-specific options** - Pass custom options to pytest

## Supported Testing Framework

| Framework  | Detection Method                   | Notes                                 |
|------------|------------------------------------| --------------------------------------|
| **pytest** | Always runs if pytest is installed | Most popular Python testing framework |

## Usage

> **Note:** Until the first release is tagged, use a specific commit SHA (e.g., `@947908a`) instead of
`@v1`. This ensures workflows continue to work even if development branches are deleted. Once v1.0.0 is
released, you can use `@v1` for the latest v1.x version.

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
          commit-badges: 'true'
          badges-directory: '.github/badges'
```

### With Badge Generation

Enable badge generation to automatically create SVG badges for pytest:

```yaml
- name: Run Python Tests
  uses: thoughtparametersllc/python-testing@v1
  with:
    commit-badges: 'true'
    badges-directory: '.github/badges'
```

When enabled, badges will show passing/failing status for pytest.

**Note:** For badge commits to work, your workflow needs `contents: write` permission:

```yaml
permissions:
  contents: write
```

## Inputs

| Input                | Description                                           | Required | Default            |
|----------------------|-------------------------------------------------------|----------|--------------------|
| `python-version`     | Python version to use for testing                     | No       | `3.x`              |
| `requirements-file`  | Path to requirements file for additional dependencies | No       | `requirements.txt` |
| `pytest-options`     | Additional options to pass to pytest                  | No       | `''`               |
| `commit-badges`      | Generate and commit SVG badges to the repository      | No       | `false`            |
| `badges-directory`   | Directory where badge SVG files will be saved         | No       | `.github/badges`   |

## How It Works

The action installs pytest and runs your tests with the specified options. You can:

1. Specify a Python version to use
2. Install additional requirements from a requirements file
3. Pass custom options to pytest
4. Generate SVG badges for test results
5. Automatically commit badges to your repository

## Examples

### pytest Project with Coverage

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov=mypackage --cov-report=xml'
```

### With Custom Requirements

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    requirements-file: 'requirements-dev.txt'
    pytest-options: '--verbose'
```

### With Badge Generation

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--verbose'
    commit-badges: 'true'
```

## Badge Display

When `commit-badges` is enabled, you can manually add badge references to your README:

```markdown
# My Project

![Pytest](.github/badges/pytest.svg)
```

The badge will automatically update with passing/failing status after each test run.

## Roadmap

Future enhancements planned:

- **Additional frameworks** - Support for unittest, nose2, behave (BDD), tox, doctest
- **Automatic README updates** - Auto-insert badge references in README
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

- [python-linting](https://github.com/thoughtparametersllc/python-linting) - Companion action for Python
  linting with pylint, black, and mypy

## Support

If you encounter any issues or have questions, please
[open an issue](https://github.com/thoughtparametersllc/python-testing/issues) on GitHub.
