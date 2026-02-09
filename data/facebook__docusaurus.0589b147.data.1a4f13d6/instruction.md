# Bug Report

### Describe the bug

When using the `data()` method to set a value on a processor instance, the method is returning the wrong value. After setting a data value with `data(key, value)`, the method returns the namespace object instead of the processor instance itself, which breaks method chaining.

### Reproduction

```js
const processor = new Processor();

// This should return the processor instance for chaining
const result = processor.data('setting', 'value');

// Expected: result === processor (for method chaining)
// Actual: result is the namespace object

// This breaks chaining like:
processor
  .data('foo', 'bar')
  .data('baz', 'qux')  // TypeError: Cannot read property 'data' of undefined
```

### Expected behavior

The `data()` method should return the processor instance when setting a value (when called with 2 arguments) to allow for method chaining, which is a common pattern in processor-based APIs.

Additionally, when getting a value with `data(key)`, it seems like the logic is inverted - it returns undefined for keys that exist in the namespace and returns the value for keys that don't exist.

### System Info
- Version: remark@15.0.1

---
Repository: /testbed
