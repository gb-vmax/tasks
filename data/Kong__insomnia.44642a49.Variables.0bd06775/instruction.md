# Bug Report

### Describe the bug

When setting variables without specifying a scope, the behavior has changed unexpectedly. Previously, `set()` would always create/update variables in the local scope, but now it seems to be searching through existing scopes and updating variables in whatever scope they already exist in.

This breaks existing workflows where we want to shadow a global or environment variable with a local value.

### Reproduction

```js
// Set up a global variable
variables.set('apiKey', 'global-key-123', 'global');

// Later in the script, try to set a local override
variables.set('apiKey', 'local-key-456');

// Expected: local variable shadows the global one
// Actual: the global variable gets updated instead
```

### Expected behavior

When calling `set()` without a scope parameter, it should always set the variable in the local scope, even if a variable with the same name exists in a higher scope (global, collection, environment, etc.). This allows for proper variable shadowing.

### Additional context

This seems to have started happening recently. The previous behavior was more predictable - local scope was always the default target when no scope was specified.

---
Repository: /testbed
