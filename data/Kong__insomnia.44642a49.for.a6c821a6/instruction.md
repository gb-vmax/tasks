# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the version control sync functionality. The application fails to start and throws an error about unexpected token or duplicate function declarations in the VCS utility module.

### Reproduction

The issue appears when the sync module is loaded. From what I can tell:

1. Start the application normally
2. Navigate to any sync-related functionality
3. The module fails to load with a syntax error

Looking at the code, it seems like there's malformed code in `packages/insomnia/src/sync/vcs/util.ts` - the `combinedMapKeys` function appears to have duplicate/nested definitions and the structure is broken.

### Expected behavior

The application should start normally and the sync functionality should be accessible without syntax errors.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
