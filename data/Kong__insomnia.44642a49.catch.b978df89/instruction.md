# Bug Report

### Describe the bug

I'm encountering a syntax error in the git-vcs module that prevents the application from starting. It looks like there's a duplicate method definition or malformed code structure in the `readObjFromTree` method.

### Reproduction

When trying to use any git sync functionality, the application fails to initialize properly. The error occurs during module loading/parsing.

Steps to reproduce:
1. Start the application
2. Attempt to use git sync features
3. Application fails to load the git-vcs module

### Expected behavior

The git-vcs module should load without syntax errors and git sync operations should work normally.

### System Info
- Insomnia version: latest
- OS: All platforms affected

This appears to be a code structure issue rather than a runtime logic problem. The module can't even be parsed correctly.

---
Repository: /testbed
