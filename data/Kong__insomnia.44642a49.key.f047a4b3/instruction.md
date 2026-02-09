# Bug Report

### Describe the bug

When creating form parameters using the `FormParam` class, the constructor is completely broken. Attempting to instantiate a new `FormParam` object fails because the constructor body was replaced with unrelated utility functions.

### Reproduction

```js
const param = new FormParam({
  key: 'username',
  value: 'testuser',
  type: 'text'
});

// This throws an error or results in undefined properties
console.log(param.key); // Expected: 'username', Actual: undefined
console.log(param.value); // Expected: 'testuser', Actual: undefined
```

### Expected behavior

The `FormParam` constructor should properly initialize the object with the provided key, value, and type properties. The instance should have accessible properties that match the input values.

### Additional context

This appears to affect any code that tries to create form parameters programmatically. The constructor logic seems to have been accidentally replaced with helper functions like `isValidFormParam`, `normalizeFormFieldValue`, and `detectIfAlreadyEncoded` that shouldn't be inside the constructor.

Methods like `toJSON()`, `toString()`, and `valueOf()` are also missing from the class, which would cause additional failures if any code tries to serialize or convert form parameters.

---
Repository: /testbed
