# Bug Report

### Describe the bug

When setting variables using the `set()` method with a specified scope parameter, the changes are not being applied to the correct scope environment. The method appears to accept a scope argument but the variable always ends up in the local scope regardless of what scope is specified.

### Reproduction

```js
const variables = new Variables(/* ... */);

// Try to set a variable in the global scope
variables.set('myVar', 'test value', 'global');

// Check where the variable actually ended up
const result = variables.getWithScope('myVar');
console.log(result.scope); // Expected: 'global', Actual: 'local'
```

### Expected behavior

When calling `set()` with a specific scope parameter (e.g., 'global', 'collection', 'environment'), the variable should be stored in that scope's environment, not always in the local scope.

### System Info
- insomnia-sdk version: latest
- The `getScopeEnvironment` helper method exists but doesn't seem to be connected properly to the `set` method

---
Repository: /testbed
