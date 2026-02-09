# Bug Report

### Describe the bug

When setting a variable without specifying a scope, the variable is not being updated in its original scope. Instead, a new variable is always created in the local scope, even if the variable already exists in a higher scope (global, collection, environment, or iterationData).

### Reproduction

```js
// Set a variable in the global scope
variables.set('apiKey', 'abc123', 'global');

// Later, try to update the same variable without specifying scope
variables.set('apiKey', 'xyz789');

// The global variable remains 'abc123'
// A new local variable 'apiKey' is created with value 'xyz789'
console.log(variables.get('apiKey')); // Returns 'xyz789' (from local scope)
// But the global scope still has the old value
```

### Expected behavior

When calling `set()` without a scope parameter on a variable that already exists in a higher scope, it should update the variable in its existing scope rather than creating a new local variable. This would maintain consistency with how variable resolution works - if `get()` finds a variable in a specific scope, `set()` should update it in that same scope.

### System Info
- insomnia-sdk version: latest
- The issue affects variable management across all scope levels (global, collection, environment, iterationData, local)

---
Repository: /testbed
