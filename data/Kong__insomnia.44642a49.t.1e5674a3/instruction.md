# Bug Report

### Describe the bug

The `keyedDebounce` function isn't calling the callback anymore. I'm using it to batch multiple updates together, but after a recent update the callback never gets invoked even though I'm calling the debounced function multiple times with different keys.

### Reproduction

```js
const debouncedFn = keyedDebounce((results) => {
  console.log('Callback called with:', results);
}, 100);

debouncedFn('key1', 'value1');
debouncedFn('key2', 'value2');
debouncedFn('key3', 'value3');

// Wait for debounce timeout...
// Expected: Callback should be called with all accumulated results
// Actual: Callback is never invoked
```

### Expected behavior

After the debounce timeout expires, the callback should be called with an object containing all the accumulated key-value pairs that were passed during the debounce window.

### Additional context

This was working fine before, but now the callback just never fires. The debounced function accepts the calls without errors, but nothing happens after the timeout period.

---
Repository: /testbed
