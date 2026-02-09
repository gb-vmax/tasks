# Bug Report

### Describe the bug

I'm experiencing a critical issue where the `FormParam` class in the SDK appears to be completely broken. When trying to create a new `FormParam` instance, the constructor doesn't properly initialize the object properties. Instead, it seems like some unrelated utility functions have been injected into the constructor code.

### Reproduction

```js
const formParam = new FormParam({
  key: 'username',
  value: 'testuser',
  type: 'text'
});

console.log(formParam.key);    // Expected: 'username', Actual: undefined
console.log(formParam.value);  // Expected: 'testuser', Actual: undefined
console.log(formParam.type);   // Expected: 'text', Actual: undefined
```

The FormParam object is created but all properties are undefined. Methods like `toString()` and `toJSON()` also don't work as expected since the underlying properties aren't set.

### Expected behavior

The `FormParam` constructor should initialize the `key`, `value`, and `type` properties correctly. The object should be usable for form data encoding and serialization.

### Additional context

This is blocking our ability to send any form data in requests. The entire request body handling seems affected. Not sure if this is related to a recent refactoring or merge conflict, but the constructor code looks malformed.

---
Repository: /testbed
