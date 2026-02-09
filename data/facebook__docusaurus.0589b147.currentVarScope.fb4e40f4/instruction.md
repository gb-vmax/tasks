# Bug Report

### Describe the bug

I'm experiencing an issue where the scope resolution appears to be accessing an out-of-bounds array index. When traversing the scope stack backwards, the loop seems to be starting at an invalid position.

### Reproduction

```js
// When currentVarScope() is called on an empty or single-element scope stack
const parser = new Parser(/* ... */);
parser.scopeStack = [{ flags: SCOPE_FUNCTION }];

// This causes the loop to start at index 1 (length) instead of 0 (length - 1)
const varScope = parser.currentVarScope();
// Expected: Should check scopeStack[0]
// Actual: Starts at scopeStack[1] which is undefined
```

### Expected behavior

The loop should start at the last valid index of the scope stack (`length - 1`) and iterate backwards through all scopes until finding one with `SCOPE_VAR` flag.

### Additional context

This seems to affect scope resolution when parsing nested blocks or function scopes. The first element in the scope stack is being skipped entirely.

---
Repository: /testbed
