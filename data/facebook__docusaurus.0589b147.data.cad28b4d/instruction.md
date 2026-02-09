# Bug Report

### Describe the bug

I'm experiencing an issue with the `data()` method when setting key-value pairs. After setting a value using `data(key, value)`, the method returns the value itself instead of returning the processor instance for method chaining.

### Reproduction

```js
const processor = unified();

// This should return the processor for chaining
const result = processor.data('settings', { some: 'value' });

// Expected: result should be the processor instance
// Actual: result is the value that was set
console.log(result === processor); // false (should be true)

// This breaks method chaining:
processor
  .data('key1', 'value1')
  .data('key2', 'value2') // TypeError: Cannot read property 'data' of undefined
  .freeze();
```

### Expected behavior

The `data()` method should return the processor instance when setting a value (when called with 2 arguments), allowing for method chaining. This is the documented behavior and how it worked previously.

### Additional context

This appears to affect the ability to chain multiple `data()` calls together, which is a common pattern when configuring the processor. The method should maintain the fluent interface pattern.

---
Repository: /testbed
