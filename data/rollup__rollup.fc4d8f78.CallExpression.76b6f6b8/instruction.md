# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining on method calls where the behavior seems inverted. When the callee evaluates to `null` or `undefined`, the call is being executed instead of being skipped, and vice versa.

### Reproduction

```js
const obj = {
  method: null
};

// This should skip the call but it's being executed
obj.method?.();

// And when method exists, it seems to be treated incorrectly
const obj2 = {
  method: function() { console.log('called'); }
};

obj2.method?.(); // Unexpected behavior here too
```

### Expected behavior

When using optional chaining with method calls:
- If the method is `null` or `undefined`, the call should be skipped entirely
- If the method exists, it should be called normally

The optional chaining operator should prevent execution when the callee is nullish.

### Additional context

This appears to affect how call expressions with optional chaining are evaluated. The skipping logic seems to be backwards from what it should be.

---
Repository: /testbed
