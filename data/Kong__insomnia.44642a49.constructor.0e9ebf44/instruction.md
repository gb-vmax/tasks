# Bug Report

### Describe the bug
When working with the Variables class, collection-level variables are not being properly initialized. It appears that collection variables are being overwritten by environment variables, causing collection-specific settings to be lost.

### Reproduction
```js
const vars = new Variables({
  globalVars: new Environment('global', { globalKey: 'globalValue' }),
  collectionVars: new Environment('collection', { collectionKey: 'collectionValue' }),
  environmentVars: new Environment('environment', { envKey: 'envValue' }),
  iterationDataVars: new Environment('iteration', {})
});

// Try to access collection variable
console.log(vars.collectionVars.get('collectionKey'));
// Expected: 'collectionValue'
// Actual: undefined

// Instead, environment variables appear in collection scope
console.log(vars.collectionVars.get('envKey'));
// Returns: 'envValue' (should be undefined)
```

### Expected behavior
Collection variables should maintain their own separate values and not be replaced by environment variables. Each variable scope (global, collection, environment, iteration) should be independent.

### Additional context
This is causing issues when trying to use collection-specific configuration that differs from environment settings. The collection variables seem to be completely ignored in favor of environment variables.

---
Repository: /testbed
