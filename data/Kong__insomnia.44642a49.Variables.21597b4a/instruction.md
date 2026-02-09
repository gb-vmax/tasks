# Bug Report

### Describe the bug
When calling the `unset` method on variables without specifying a scope, it removes the variable from all scopes where it exists. However, when a scope is specified, the method returns early without properly unsetting the variable, causing the variable to remain in the specified scope.

### Reproduction
```js
const vars = new Variables(/* ... */);

// Set a variable in global scope
vars.set('myVar', 'test', 'global');

// Try to unset it from global scope
vars.unset('myVar', 'global');

// The variable is still accessible
console.log(vars.get('myVar')); // Still returns 'test' instead of undefined
```

### Expected behavior
When `unset` is called with a specific scope, it should remove the variable from that scope. The variable should no longer be accessible via `get()` unless it exists in another scope with higher precedence.

### Additional context
The issue appears when trying to remove variables from specific scopes like 'global', 'collection', 'environment', etc. The unset operation doesn't complete properly when a scope parameter is provided.

---
Repository: /testbed
