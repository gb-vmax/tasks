# Bug Report

### Describe the bug

I'm experiencing a syntax error in the git-vcs module that's preventing the application from starting. It looks like there's a malformed try-catch block in the `readObjFromTree` method.

### Reproduction

1. Start the application
2. Try to perform any git sync operation
3. Application fails to load/crashes with a syntax error

The error seems to be related to the git VCS module around line 535. When I look at the code, the try-catch block appears to be incomplete or incorrectly structured - there's a function definition (`processDataItems`) inserted in the middle of the catch block which doesn't make sense.

### Expected behavior

The application should start normally and git sync operations should work without syntax errors.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is blocking all git sync functionality. Any help would be appreciated!

---
Repository: /testbed
