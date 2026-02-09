# Bug Report

### Describe the bug

I'm experiencing an issue with the `Variables` class where the `has()` method doesn't check for variables in the local scope. When I set a variable using `set()`, calling `has()` on that same variable returns `false` even though the variable exists.

### Reproduction

```js
const vars = new Variables(/* ... */);

// Set a local variable
vars.set('myVar', 'test value');

// Check if it exists
console.log(vars.has('myVar')); // Expected: true, Actual: false
```

The `has()` method seems to only check global, collection, environment, and iteration data variables, but completely ignores local variables that were set using the `set()` method.

### Expected behavior

When a variable is set using `set()`, the `has()` method should return `true` for that variable name. Local variables should be included in the existence check.

### Additional context

This makes it difficult to determine if a variable exists before trying to retrieve it, especially when working with locally scoped variables. The `get()` method appears to work correctly and can retrieve local variables, so it's inconsistent that `has()` doesn't check the same scope.

---
Repository: /testbed
