# Bug Report

### Describe the bug

After a recent update, the application fails to start due to a syntax error in the test setup file. The error appears to be related to malformed JavaScript object syntax in the global.main configuration.

### Reproduction

1. Try to run the application or any tests
2. The process fails immediately with a syntax error
3. Error points to the `__jest__/setup.ts` file

The issue seems to be in the global.main object definition where there's invalid syntax mixing function definitions and object properties.

### Expected behavior

The application should start normally and the test setup should initialize without syntax errors. The global.main object should be properly structured with all its methods defined correctly.

### System Info
- Package: @insomnia/insomnia
- Node version: (any)

This is blocking all development work as nothing can run with this syntax error present. Would appreciate a quick fix!

---
Repository: /testbed
