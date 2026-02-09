# Bug Report

### Describe the bug

When logging errors with a `cause` property, only the first level cause is being displayed in the error output. If the cause itself has a nested `cause`, it's not being shown in the error chain.

### Reproduction

```js
const error = new Error('Main error');
error.cause = new Error('First cause');
error.cause.cause = new Error('Root cause');

// Only the main error and first cause are logged
// The root cause is missing from the output
handleError(error);
```

### Expected behavior

The error handler should traverse and display the entire cause chain, showing all nested causes in the error output. Each level of the cause chain should be indented appropriately to show the hierarchy.

For example, the output should show:
- Main error
- [cause] First cause  
- [cause] Root cause

But currently it only shows the first cause and stops there.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
