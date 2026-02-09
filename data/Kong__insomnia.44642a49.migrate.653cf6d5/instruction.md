# Bug Report

### Describe the bug

After a recent update, the application crashes on startup with a syntax error. The environment model seems to have an incomplete function definition that's causing the entire module to fail to load.

### Reproduction

1. Start the application
2. Application fails to load with a JavaScript syntax error
3. Error points to the environment.ts model file

The issue appears to be in the `isValidColor` function at the bottom of the file - it looks like the function body is incomplete or got cut off during editing.

### Expected behavior

The application should start normally without any syntax errors. The environment model should load successfully and all environment-related functionality should work as expected.

### System Info
- Insomnia version: latest
- OS: Any

This is blocking us from using the application at all since it can't even start up. Would appreciate a quick fix!

---
Repository: /testbed
