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

That's it! The action will install pytest and run your tests.

## Testing Framework

This action runs pytest for your Python tests.

### pytest

The action installs and runs pytest with your specified options.

**Example configuration:**
```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov=mypackage --cov-report=xml'
```

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

### pytest Options

Pass custom options to pytest:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: '--cov --cov-report=xml --maxfail=1'
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
          commit-badges: 'true'
          badges-directory: '.github/badges'
```

### Manual Badge Reference

Add badges manually to your README:

```markdown
# My Project

![Pytest](.github/badges/pytest.svg)
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

### Conditional Testing

Run different options on different branches:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    pytest-options: ${{ github.ref == 'refs/heads/main' && '--cov --slow' || '--fast' }}
```

## Troubleshooting

### Badge Commit Failures

If badges aren't being committed:

1. Ensure `contents: write` permission is granted:
   ```yaml
   permissions:
     contents: write
   ```

2. Check that the branch is not protected without allowing bot commits

3. Verify the action has access to push to the repository

### Installation Issues

If pytest or requirements fail to install:

1. Check that `requirements-file` path is correct
2. Verify your requirements file has correct syntax
3. Look for conflicting package versions
4. Try specifying an explicit Python version

### Tests Failing

To debug test failures:

1. Review the detailed output in the GitHub Actions summary
2. Run tests locally with the same options
3. Check for environment-specific issues (paths, dependencies)
4. Enable verbose output:
   ```yaml
   pytest-options: '--verbose --tb=long'
   ```

### Custom Test Directories

If tests are in a non-standard location:

```yaml
pytest-options: 'path/to/tests/'
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
