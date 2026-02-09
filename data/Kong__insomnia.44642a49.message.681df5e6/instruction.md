# Bug Report

### Describe the bug

Getting a runtime error when trying to use merge conflict functionality. The application crashes with a TypeError saying that something is not a function.

### Reproduction

```js
// When a merge conflict occurs and the schema tries to generate default values
const conflict = {
  ...mergeConflictSchema
};

// Accessing the message property triggers the error
const msg = conflict.message();
```

### Expected behavior

The `message` property should return a string value 'message' without throwing any errors. The merge conflict schema should be able to generate default values properly.

### System Info
- Version: Latest from main branch
- Node version: 18.x

This seems to have broken recently, possibly after a recent change to the type schemas file. The error appears when the sync functionality tries to handle merge conflicts.

---
Repository: /testbed
