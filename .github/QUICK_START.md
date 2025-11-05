# Quick Start Guide

Get started with Python Testing Action in minutes!

## 1. Basic Setup (2 minutes)

Create `.github/workflows/test.yml`:

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

Commit and push. Done! 🎉

## 2. With Badges (5 minutes)

Update your workflow to include badges:

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: thoughtparametersllc/python-testing@v1
        with:
          generate-badges: 'true'
          update-readme: 'true'
```

Badges will automatically appear in your README! 🏷️

## 3. With Custom Options (10 minutes)

Add framework-specific options:

```yaml
- uses: thoughtparametersllc/python-testing@v1
  with:
    python-version: '3.11'
    requirements-file: 'requirements.txt'
    pytest-options: '--cov --cov-report=xml'
    behave-options: '--format=progress'
```

## What Happens Automatically?

✅ Detects your testing frameworks  
✅ Installs necessary dependencies  
✅ Runs all detected tests  
✅ Generates detailed reports  
✅ Creates status badges (if enabled)  
✅ Updates README (if enabled)  

## Supported Frameworks

- **pytest** - Most popular Python testing framework
- **unittest** - Built-in Python testing
- **nose2** - Enhanced testing
- **behave** - BDD/Cucumber-style testing
- **tox** - Multi-environment testing
- **doctest** - Documentation testing

## Next Steps

- Read the [Usage Guide](USAGE.md) for detailed configuration
- Check [example workflows](workflows/) for more ideas
- Review the [README](../README.md) for complete documentation

## Need Help?

- See [Troubleshooting](USAGE.md#troubleshooting) section
- [Open an issue](https://github.com/thoughtparametersllc/python-testing/issues)
