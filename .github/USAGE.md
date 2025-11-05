# Python Testing Action - Usage Guide

This guide provides detailed information on using the Python Testing GitHub Action.

## Table of Contents

- [Quick Start](#quick-start)
- [Framework Detection](#framework-detection)
- [Configuration Options](#configuration-options)
- [Badge Generation](#badge-generation)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)

## Quick Start

Add this workflow to your repository (`.github/workflows/test.yml`):

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: thoughtparametersllc/python-testing@v1
```

That's it! The action will automatically detect and run your testing frameworks.

## Framework Detection

The action automatically detects which testing frameworks your project uses:

### pytest

Detected if any of these exist:
- `pytest.ini` file
- `pyproject.toml` file
- `setup.cfg` file
- `import pytest` in any Python file

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov=mypackage --cov-report=xml'
```

### unittest

Detected if:
- `import unittest` found in test files (test*.py or *test.py)

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    unittest-options: '-v -s tests'
```

### nose2

Detected if any of these exist:
- `.noserc` file
- `nose.cfg` file
- `[nosetests]` section in `setup.cfg`

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    nose-options: '--verbose --with-coverage'
```

### behave (BDD/Cucumber)

Detected if:
- `features/` directory exists with `.feature` files

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    behave-options: '--format=progress --tags=@automated'
```

### tox

Detected if:
- `tox.ini` file exists

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    tox-options: '-e py311,py312'
```

### doctest

Detected if:
- `>>>` patterns found in Python files (indicating docstring tests)

## Configuration Options

### Python Version

Specify the Python version to use:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    python-version: '3.11'
```

### Requirements File

Install additional dependencies before running tests:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    requirements-file: 'requirements-dev.txt'
```

### Framework-Specific Options

Pass custom options to each testing framework:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov --cov-report=xml --maxfail=1'
    unittest-options: '-v -s tests'
    nose-options: '--verbose --with-timer'
    behave-options: '--tags=@smoke --format=pretty'
    tox-options: '-e py311'
```

## Badge Generation

### Enabling Badges

Generate SVG badges showing test status:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # Required for badge commits
    
    steps:
      - uses: actions/checkout@v4
      
      - uses: thoughtparametersllc/python-testing@v1
        with:
          generate-badges: 'true'
          badges-directory: '.github/badges'
```

### Automatic README Updates

Automatically insert badge references in your README:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    generate-badges: 'true'
    update-readme: 'true'
    readme-path: 'README.md'
    badge-style: 'path'  # or 'url'
```

### Badge Styles

Two badge styles are available:

1. **Relative Path** (`badge-style: 'path'`):
   ```markdown
   ![Pytest](.github/badges/pytest.svg)
   ```

2. **GitHub URL** (`badge-style: 'url'`):
   ```markdown
   ![Pytest](https://raw.githubusercontent.com/owner/repo/main/.github/badges/pytest.svg)
   ```

### Manual Badge Reference

If not using automatic README updates, add badges manually:

```markdown
# My Project

![Pytest](.github/badges/pytest.svg)
![Unittest](.github/badges/unittest.svg)
![Behave](.github/badges/behave.svg)
```

## Advanced Usage

### Matrix Testing

Test across multiple Python versions:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
    
    steps:
      - uses: actions/checkout@v4
      - uses: thoughtparametersllc/python-testing@v1
        with:
          python-version: ${{ matrix.python-version }}
```

### Multiple Operating Systems

Test on different operating systems:

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.9', '3.11']
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      - uses: thoughtparametersllc/python-testing@v1
        with:
          python-version: ${{ matrix.python-version }}
```

### Coverage Reports

Generate coverage reports with pytest:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov=mypackage --cov-report=xml --cov-report=html'

- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
```

### BDD Testing with Behave

Run specific feature tags:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    behave-options: '--tags=@smoke,@critical --format=progress'
```

### Conditional Testing

Run different frameworks on different branches:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: ${{ github.ref == 'refs/heads/main' && '--cov --slow' || '--fast' }}
```

## Troubleshooting

### No Frameworks Detected

If no frameworks are detected:

1. Check that your test files are in the repository
2. Verify framework configuration files exist
3. Ensure test imports are present in your code
4. Review the detection summary in the Action output

### Badge Commit Failures

If badges aren't being committed:

1. Ensure `contents: write` permission is granted:
   ```yaml
   permissions:
     contents: write
   ```

2. Check that the branch is not protected without allowing bot commits

3. Verify the action has access to push to the repository

### Framework Installation Issues

If a framework fails to install:

1. Check that `requirements-file` path is correct
2. Verify your requirements file has correct syntax
3. Look for conflicting package versions
4. Try specifying an explicit Python version

### Tests Failing

To debug test failures:

1. Review the detailed output in the GitHub Actions summary
2. Run tests locally with the same options
3. Check for environment-specific issues (paths, dependencies)
4. Enable verbose output with framework options:
   ```yaml
   pytest-options: '--verbose --tb=long'
   unittest-options: '-v'
   ```

### Custom Test Directories

If tests are in a non-standard location:

For pytest:
```yaml
pytest-options: 'path/to/tests/'
```

For unittest:
```yaml
unittest-options: '-s path/to/tests'
```

## Best Practices

1. **Use a requirements file**: Specify all test dependencies
2. **Enable coverage**: Track test coverage with appropriate options
3. **Use badges**: Show test status in your README
4. **Matrix testing**: Test across multiple Python versions
5. **Fail fast**: Use `--maxfail=1` for pytest to stop on first failure
6. **Verbose output**: Enable verbose mode for debugging

## Examples Repository

See the [.github/workflows/](./../workflows/) directory for example workflow configurations.

## Support

If you need help:
- Check the [README](../../README.md)
- Review [example workflows](./../workflows/)
- [Open an issue](https://github.com/thoughtparametersllc/python-testing/issues)
