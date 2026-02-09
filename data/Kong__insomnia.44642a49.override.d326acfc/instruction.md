# Bug Report

### Describe the bug

The `valueOf()` method on `Header` objects is returning an unexpected object structure instead of the primitive value. When accessing header values through `valueOf()`, I'm getting `{ primitive: <value> }` instead of just the value itself.

### Reproduction

```js
const header = new Header({
  key: 'Content-Type',
  value: 'application/json'
});

// Expected: 'application/json'
// Actual: { primitive: 'application/json' }
console.log(header.valueOf());
```

### Expected behavior

`valueOf()` should return the primitive string value directly, not wrapped in an object. This is breaking code that relies on implicit type coercion or direct value comparison.

For example:
```js
const headerValue = header.valueOf();
console.log(headerValue); // Should be: 'application/json'
console.log(typeof headerValue); // Should be: 'string'
```

### Additional context

This seems to have changed recently. Previously `valueOf()` returned the raw value, which is the standard behavior for `valueOf()` methods in JavaScript. The current implementation breaks compatibility with code expecting primitive values.

---
Repository: /testbed
