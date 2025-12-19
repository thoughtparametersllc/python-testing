# Security Policy

## Supported Versions

We actively support the following versions of this GitHub Action:

| Version | Supported          |
| ------- | ------------------ |
| v1.x    | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of this GitHub Action seriously. If you discover a security vulnerability, please follow these steps:

### Where to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to:

- **Email**: [jason.miller@thoughtparameters.com](mailto:jason.miller@thoughtparameters.com)
- **Subject**: Security Vulnerability in python-unit-testing action

### What to Include

Please include the following information in your report:

1. **Description**: A clear description of the vulnerability
2. **Impact**: What an attacker could achieve by exploiting this vulnerability
3. **Reproduction Steps**: Detailed steps to reproduce the issue
4. **Affected Versions**: Which versions of the action are affected
5. **Suggested Fix**: If you have ideas on how to fix the issue (optional)

### Response Timeline

- **Initial Response**: Within 48 hours of receiving your report
- **Status Update**: Within 7 days with an assessment of the vulnerability
- **Fix Timeline**: We aim to release a fix within 30 days for critical issues

### Disclosure Policy

- Please allow us reasonable time to address the vulnerability before public disclosure
- We will acknowledge your contribution in the security advisory (if you wish)
- We may provide a CVE identifier for significant vulnerabilities

## Security Best Practices for Users

When using this action in your workflows:

1. **Pin to Specific Versions**: Use specific version tags (e.g., `@v1.0.0`) rather than floating tags
   when possible for production workflows
2. **Review Permissions**: Only grant necessary permissions to the workflow:

   ```yaml
   permissions:
     contents: write  # Only needed if commit-badges is enabled
   ```

3. **Protect Secrets**: Never pass secrets or credentials through action inputs
4. **Review Dependencies**: Check the `requirements-file` for untrusted packages
5. **Use Branch Protection**: Enable branch protection to prevent unauthorized badge commits

## Known Security Considerations

### Badge Commits

When `commit-badges` is enabled:

- The action will commit SVG badge files to your repository
- It uses the `github-actions[bot]` account for commits
- Commits include `[skip ci]` to prevent infinite workflow loops
- Requires `contents: write` permission

**Mitigation**: Only enable badge commits if you trust the test results and understand the implications.

### Dependencies

This action installs:

- pytest from PyPI
- Your specified requirements file packages

**Mitigation**:

- Review your requirements file for known vulnerabilities
- Use tools like `pip-audit` or `safety` to scan dependencies
- Pin package versions in your requirements file

## Security Updates

Security updates will be released as:

1. **Patch releases** for minor security issues
2. **Minor releases** for moderate security issues
3. **Major releases** for critical security issues with breaking changes

We will publish security advisories through GitHub Security Advisories.

## Additional Resources

- [GitHub Actions Security Best Practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Securing GitHub Actions](https://docs.github.com/en/actions/security-guides)

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities.
Contributors who report valid security issues will be acknowledged (with permission) in our security
advisories and release notes.
