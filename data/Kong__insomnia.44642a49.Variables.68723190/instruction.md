# Bug Report

### Describe the bug
When setting variables at different scopes (local, environment, collection, global), the variable resolution order seems incorrect. Variables that should be overridden by more specific scopes are being ignored.

### Reproduction
```js
// Set a global variable
pm.globals.set('apiKey', 'global-key');

// Set the same variable at environment level
pm.environment.set('apiKey', 'env-key');

// Set the same variable at local level
pm.variables.set('apiKey', 'local-key');

// Try to get the variable
const value = pm.variables.get('apiKey');
console.log(value); // Expected: 'local-key', but getting 'global-key'
```

### Expected behavior
Variables should follow the standard precedence order where local variables take highest priority, followed by iteration data, environment, collection, and finally global variables. The most specific scope should always win when multiple scopes define the same variable name.

In the example above, `pm.variables.get('apiKey')` should return `'local-key'` since local scope has the highest priority.

### Additional context
This affects variable resolution across all request scripts and tests. It seems like the priority order might be inverted somehow.

---
Repository: /testbed
