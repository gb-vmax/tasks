# Bug Report

### Describe the bug
The `has()` method in the Variables class is not working correctly. When checking if a variable exists in any of the variable scopes (global, collection, environment, iteration data, or local), it only returns `true` if the variable exists in ALL scopes instead of ANY scope.

### Reproduction
```js
const vars = new Variables({
  globalVars: new Map([['globalVar', 'value1']]),
  collectionVars: new Map(),
  environmentVars: new Map(),
  iterationDataVars: new Map(),
  localVars: new Map()
});

// This returns false even though 'globalVar' exists in global scope
console.log(vars.has('globalVar')); // Expected: true, Actual: false
```

### Expected behavior
The `has()` method should return `true` if a variable exists in ANY of the variable scopes (global, collection, environment, iteration data, or local), not only when it exists in ALL scopes.

Additionally, the `get()` method seems to have inverted logic - it's checking if `finalVal` is truthy before assigning a new value, which means it will skip the first found value and only assign subsequent ones.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
