# Quick Start Guide

Get started with Python Unit Testing Action in minutes!

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
      - uses: thoughtparametersllc/python-unit-testing@v1
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
      - uses: thoughtparametersllc/python-unit-testing@v1
        with:
          commit-badges: 'true'
```

Then add badge to your README manually:

```markdown
![Pytest](.github/badges/pytest.svg)
```

## 3. With Custom Options (10 minutes)

Add pytest-specific options:

```yaml
- uses: thoughtparametersllc/python-unit-testing@v1
  with:
    python-version: '3.11'
    requirements-file: 'requirements.txt'
    pytest-options: '--cov --cov-report=xml'
```

## What Happens Automatically?

✅ Installs pytest  
✅ Installs your requirements  
✅ Runs pytest tests  
✅ Generates detailed reports  
✅ Creates status badges (if enabled)  

## Supported Framework

- **pytest** - Most popular Python testing framework

## Next Steps

- Read the [Usage Guide](USAGE.md) for detailed configuration
- Check [example workflows](workflows/) for more ideas
- Review the [README](../README.md) for complete documentation

## Need Help?

- See [Troubleshooting](USAGE.md#troubleshooting) section
- [Open an issue](https://github.com/thoughtparametersllc/python-unit-testing/issues)
