# Bug Report

### Describe the bug

I'm experiencing a syntax error in the merge conflict schema definition. After a recent update, the application fails to start due to what appears to be a malformed schema object.

### Reproduction

The issue occurs when trying to initialize the sync module. The `mergeConflictSchema` object seems to have invalid syntax - there's a function definition (`createUniqueKeyContext`) appearing where it shouldn't be, and the `key` property is followed by a `choose` property without proper object structure.

Looking at the schema definition, it appears that:
1. An `export` statement is placed inside the schema object
2. The `key` property definition is not properly closed before the `choose` property

This causes the module to fail to load entirely.

### Expected behavior

The `mergeConflictSchema` should be a valid Schema object with properly structured properties like `key`, `choose`, `mineBlob`, etc. The schema should load without syntax errors and allow the sync functionality to work correctly.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is blocking our ability to use the sync features. Any help would be appreciated!

---
Repository: /testbed
