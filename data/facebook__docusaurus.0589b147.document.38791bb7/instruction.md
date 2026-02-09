# Bug Report

### Describe the bug

The application crashes on startup with a syntax error in the remark vendor bundle. It appears there's corrupted or invalid JavaScript code in the constructs exports section.

### Reproduction

1. Start the application
2. The bundle fails to load with a syntax error

The error occurs in `jest/vendor/remark@15.0.1.js` where there seems to be invalid syntax in the exports definition. Instead of proper JavaScript code, there are numeric literals that break the module.

### Expected behavior

The application should start normally and the remark vendor bundle should load without syntax errors.

### Additional context

This looks like it might be a corruption in the vendor file or an issue with how the bundle was generated. The file was working previously, so this appears to be a recent regression.

---
Repository: /testbed
