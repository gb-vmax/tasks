# Bug Report

### Describe the bug

I'm experiencing an issue with variable resolution in the Insomnia SDK. When I set variables at different scopes (local, environment, collection, global), the wrong variable value is being returned when I call `get()`.

### Reproduction

```js
const vars = new Variables();

// Set variables at different scopes
vars.globalVars.set('myVar', 'global_value');
vars.environmentVars.set('myVar', 'environment_value');
vars.localVars.set('myVar', 'local_value');

// Expected: 'local_value' (local scope should have highest priority)
// Actual: 'global_value' (global scope is being used instead)
console.log(vars.get('myVar'));
```

### Expected behavior

According to the documentation, variable resolution should follow this priority order:
1. Local variables (highest priority)
2. Iteration data variables
3. Environment variables
4. Collection variables
5. Global variables (lowest priority)

The `get()` method should return the value from the highest priority scope where the variable is defined. In the example above, it should return `'local_value'` since local scope has the highest priority.

### Additional context

This seems to have broken recently. The variable scoping behavior is critical for our use case where we need to override global/collection variables with environment or local values.

---
Repository: /testbed
