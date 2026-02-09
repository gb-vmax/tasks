# Bug Report

### Describe the bug

After updating to the latest version, plugin installation is failing with errors being incorrectly classified as deprecation warnings. The installation process now treats legitimate error messages as warnings and continues, causing plugins to fail silently instead of properly reporting the error.

### Reproduction

When trying to install a plugin that has an actual error (not just a deprecation warning), the error gets misclassified and the installation appears to succeed even though it shouldn't.

For example, if npm/yarn returns an error message containing words like "deprecated" or "security" along with phrases like "please upgrade", the error is now being treated as just a warning instead of a real error.

This causes the installation to proceed when it should actually fail, leading to broken plugin installations that appear successful in the UI.

### Expected behavior

Only actual deprecation warnings should be treated as warnings. Real errors should be properly identified and cause the installation to fail, even if they contain keywords like "deprecated" or "security" in the error message.

The previous behavior was more strict and only allowed very specific deprecation message patterns to pass through. Now it seems too permissive and catches too many cases.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
