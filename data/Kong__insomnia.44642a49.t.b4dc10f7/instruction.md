# Bug Report

### Describe the bug

The `keyedDebounce` function is not working correctly - the callback is being invoked with an empty results object instead of the accumulated results. When multiple debounced calls are made with different keys, the callback receives `{}` instead of the expected key-value pairs.

### Reproduction

```js
const debouncedFn = keyedDebounce((results) => {
  console.log('Results:', results);
  // Expected: { key1: ['value1'], key2: ['value2'] }
  // Actual: {}
}, 100);

debouncedFn('key1', 'value1');
debouncedFn('key2', 'value2');

// Wait for debounce to trigger...
// Console shows: Results: {}
```

### Expected behavior

The callback should receive an object containing all the accumulated key-value pairs that were collected during the debounce period. In the example above, it should log `{ key1: ['value1'], key2: ['value2'] }` instead of an empty object.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
