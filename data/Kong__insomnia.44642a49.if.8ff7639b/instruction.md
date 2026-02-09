# Bug Report

### Describe the bug

The `withDescendants` function appears to have duplicate code after a recent change. When trying to use this function, it's causing syntax errors because the function is defined twice in the same scope.

### Reproduction

```typescript
// Attempting to call withDescendants
const descendants = await database.withDescendants(doc, 'stopType');
```

This results in parsing errors because the function signature is duplicated.

### Expected behavior

The function should be defined only once and execute normally without syntax errors. It should return all descendants of a given document as it did before.

### Additional context

Looking at the code, it seems like there are two function definitions for `withDescendants` - one with the new parameters (`maxDepth`, `typesToInclude`) and one with the original implementation. The old implementation code appears right after the new one, causing a conflict.

This is preventing the application from even starting up properly.

---
Repository: /testbed
