# Bug Report

### Describe the bug

When retrieving data from the processor's namespace using the `data()` method with a string key, falsy values (like `false`, `0`, empty string `""`, etc.) are being returned as `undefined` instead of their actual values.

### Reproduction

```js
const processor = unified()

// Set a falsy value
processor.data('myFlag', false)
processor.data('count', 0)
processor.data('emptyString', '')

// Try to retrieve them
console.log(processor.data('myFlag'))       // Expected: false, Got: undefined
console.log(processor.data('count'))        // Expected: 0, Got: undefined
console.log(processor.data('emptyString'))  // Expected: "", Got: undefined
```

### Expected behavior

The `data()` method should return the actual stored value, even when it's falsy. Only keys that don't exist in the namespace should return `undefined`.

### Additional context

This seems to affect any falsy value stored in the processor's data namespace. Truthy values work as expected, but falsy values are incorrectly treated as non-existent.

---
Repository: /testbed
