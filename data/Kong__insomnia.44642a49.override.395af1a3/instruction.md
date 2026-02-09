# Bug Report

### Describe the bug

I'm experiencing an issue with the `Header` class where calling `valueOf()` returns the wrong value. When I try to use a Header object in contexts that expect a primitive value (like string concatenation or comparison), I'm getting the entire Header object instead of just its value string.

### Reproduction

```js
const header = new Header({
  key: 'Content-Type',
  value: 'application/json'
});

// This should return 'application/json' but returns the Header object
console.log(header.valueOf());

// String coercion doesn't work as expected
const result = 'Value is: ' + header;
// Expected: 'Value is: application/json'
// Actual: 'Value is: [object Object]'
```

### Expected behavior

The `valueOf()` method should return the primitive string value of the header (i.e., `this.value`), not the Header object itself. This would allow the Header object to be properly coerced to a string in operations like concatenation and comparisons.

### System Info
- insomnia-sdk version: latest

---
Repository: /testbed
