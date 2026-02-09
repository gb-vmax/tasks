# Bug Report

### Describe the bug

I'm experiencing a syntax error in the VCS util module that's preventing the application from running. It appears there's a malformed code structure where function definitions are nested incorrectly within a for loop.

### Reproduction

The issue occurs when trying to use any VCS-related functionality. The code fails to parse/compile due to invalid syntax in `packages/insomnia/src/sync/vcs/util.ts`.

Steps to reproduce:
1. Start the application
2. Attempt to use any sync/VCS features
3. Application fails to load or throws a syntax error

### Expected behavior

The `describeChanges` function should properly analyze differences between two model objects and return a list of changed properties. The function should compile without syntax errors.

### Current behavior

The code has nested function definitions inside a for loop that breaks the control flow. The original `shouldIgnoreKey` check appears to have been replaced with function definitions, but the structure is incomplete/malformed.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This looks like it might have been introduced during a refactoring or merge conflict that wasn't properly resolved. The code structure suggests someone was adding support for nested object and array change detection but didn't complete the implementation correctly.

---
Repository: /testbed
