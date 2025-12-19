# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- SECURITY.md file with security policy and vulnerability reporting guidelines
- .markdownlint.json configuration file for consistent markdown formatting
- Comprehensive security best practices documentation

### Changed

- Updated README.md to accurately reflect actual action.yml inputs and functionality
- Updated README.md description from "automatically detect and run Python testing frameworks" to
  "run Python tests using pytest"
- Updated USAGE.md to match current pytest-only implementation
- Updated USAGE.md to clarify the action installs pytest and runs tests (not automatic detection)
- Updated QUICK_START.md to reflect actual badge generation workflow
- Updated IMPLEMENTATION_SUMMARY.md to accurately reflect pytest-only implementation
- Fixed CONTRIBUTING.md references from "Python Linting Action" to "Python Testing Action"
- Fixed clone path in CONTRIBUTING.md from "python-linting" to "python-testing"
- Removed documentation for non-existent inputs: unittest-options, nose-options, behave-options,
  tox-options, generate-badges, update-readme, readme-path, and badge-style
- Updated feature list to reflect pytest-only support
- Simplified framework detection section to reflect current implementation

### Fixed

- Documentation inconsistencies between action.yml and README.md
- Incorrect action name references in CONTRIBUTING.md

## [1.0.1] - 2025-12-19

Patch release with documentation improvements

## [1.0.0] - 2025-12-19

Initial release with pytest support

## [0.0.1] - 2025-12-19

Initial development release
