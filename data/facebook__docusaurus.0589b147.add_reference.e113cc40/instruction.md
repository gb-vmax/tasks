# Bug Report

### Describe the bug

I'm experiencing an issue where the application crashes with a `TypeError: Cannot read properties of undefined (reading 'add')` when processing MDX files with certain variable references. This seems to happen when the scope chain is being traversed during reference analysis.

### Reproduction

When processing an MDX file with nested scopes and variable references, the application throws an error during the compilation phase. This occurs specifically when analyzing expressions that involve variable references in nested scope contexts.

Example scenario that triggers the issue:
1. Have an MDX file with nested function scopes
2. Reference a variable from an outer scope
3. The compiler attempts to add the reference to the scope chain
4. Error is thrown when trying to add to an undefined scope's references

The error message indicates that it's trying to call `.add()` on something that doesn't exist, suggesting the scope object is undefined at some point during the traversal.

### Expected behavior

The compiler should successfully analyze variable references across nested scopes without throwing errors. References should be properly tracked in the scope chain even when traversing from inner to outer scopes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression as it was working fine previously. The issue appears to be in the reference tracking logic during scope analysis.

---
Repository: /testbed
