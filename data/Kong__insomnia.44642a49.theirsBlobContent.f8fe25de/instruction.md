# Bug Report

### Describe the bug

There seems to be a syntax error in the merge conflict schema that's breaking the application. When trying to use sync functionality, the app crashes with a parsing error.

### Reproduction

1. Try to access any sync-related functionality
2. The application fails to load/initialize properly
3. Console shows syntax errors related to schema parsing

It looks like the `theirsBlobContent` property in the merge conflict schema has some malformed code. The schema definition appears to be incomplete or corrupted - there's a function definition that starts but doesn't properly close, and the property assignment syntax is broken.

### Expected behavior

The merge conflict schema should properly define the `theirsBlobContent` property as a function that returns null (like the other blob content properties), and the application should load without syntax errors.

### System Info
- Insomnia version: latest
- OS: N/A (code issue)

---
Repository: /testbed
