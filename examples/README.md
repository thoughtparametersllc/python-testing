# Testing Examples

This directory contains example projects demonstrating different testing frameworks supported by the Python Testing Action.

## Examples

### pytest_example
Demonstrates pytest with test discovery and fixtures.

### unittest_example
Demonstrates Python's built-in unittest framework.

### behave_example
Demonstrates BDD-style testing with behave (Cucumber for Python).

### mixed_example
Demonstrates a project using multiple testing frameworks.

## Using These Examples

Each example can be used as a reference for setting up your own tests:

1. Copy the structure to your project
2. Adapt the tests to your needs
3. Use the Python Testing Action in your workflow
4. The action will automatically detect and run the appropriate tests

## Testing Locally

You can test these examples locally:

```bash
cd pytest_example
pip install pytest
pytest

cd ../unittest_example
python -m unittest discover

cd ../behave_example
pip install behave
behave

cd ../mixed_example
pip install pytest
pytest
```

## GitHub Actions Integration

Each example works automatically with:

```yaml
- uses: thoughtparametersllc/python-testing@v1
```

No additional configuration needed!
