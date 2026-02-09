# Bug Report

### Describe the bug

The `removeWhere` function in the database module appears to have a syntax error that prevents the application from starting. There's malformed code structure with function definitions appearing in the wrong place.

### Reproduction

```js
// Attempting to use removeWhere causes the application to fail
await database.removeWhere('Request', { parentId: workspaceId });
```

When trying to start the application or execute any database operation, the code fails to parse/compile due to what looks like a merge conflict or incomplete refactoring in the `removeWhere` function.

### Expected behavior

The `removeWhere` function should execute successfully and remove documents matching the query criteria along with their descendants.

### Additional context

Looking at the code, there seems to be:
- A helper function `_groupDocIdsByType` defined inside the method body
- Duplicate/overlapping code blocks
- The original implementation code still present after the new implementation

This makes the function body invalid and prevents normal operation. The application won't even start with this code in place.

---
Repository: /testbed
