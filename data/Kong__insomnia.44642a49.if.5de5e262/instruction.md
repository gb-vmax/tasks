# Bug Report

### Describe the bug

After a recent update, the application fails to start with a syntax error in the VCS utility module. It appears there's a duplicate function declaration issue in `packages/insomnia/src/sync/vcs/util.ts`.

### Reproduction

1. Pull the latest changes
2. Try to start the application
3. Application crashes with a syntax error

The error occurs in the `generateStateMap` function where there seems to be overlapping code that prevents the module from loading properly.

### Expected behavior

The application should start normally without any syntax errors. The `generateStateMap` function should be properly defined once with the appropriate signature.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
