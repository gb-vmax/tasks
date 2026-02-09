# Bug Report

### Describe the bug

The `set` method in the Variables class is not working correctly when trying to set variables in different scopes. When I call `set` with a scope option other than 'local', the method throws an error because `getScopeEnvironment` is defined as a private method on the wrong class.

### Reproduction

```js
const variables = new Variables({
  globalVars: new Environment(),
  collectionVars: new Environment(),
  environmentVars: new Environment(),
  iterationDataVars: new Environment(),
  localVars: new Environment()
});

// This fails with an error
variables.set('myVar', 'value', { scope: 'global' });
```

### Expected behavior

The variable should be set in the global scope without any errors. The `set` method should be able to access different environment scopes (global, collection, environment, iteration, local) based on the scope option provided.

### Additional context

This issue appeared after the recent refactoring that added support for setting variables in different scopes. The code tries to call `this.getScopeEnvironment(scope)` but the method doesn't exist on the Variables class where it's being called from.

---
Repository: /testbed
