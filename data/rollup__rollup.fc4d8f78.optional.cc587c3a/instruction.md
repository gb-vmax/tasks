# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions. When using the `?.()` syntax for optional function calls, the behavior appears to be inverted - calls that should be treated as optional are being treated as non-optional, and vice versa.

### Reproduction

```js
const obj = {
  method: () => console.log('called')
};

// Optional call - should safely handle if method doesn't exist
obj.method?.();

// vs regular call
obj.method();
```

The optional call expression seems to be evaluated incorrectly. When I use `?.()`, it's behaving as if it's a regular call, and regular calls are being treated as optional.

### Expected behavior

Optional chaining with `?.()` should:
- Only invoke the function if it exists
- Return undefined if the function doesn't exist
- Not throw an error when the property is null/undefined

Regular calls without `?.()` should:
- Always attempt to invoke the function
- Throw an error if the property is not a function

### Additional context

This is causing issues in my code where I'm trying to safely call potentially undefined callback functions. The logic appears to be backwards from what the optional chaining operator is supposed to do.

---
Repository: /testbed
