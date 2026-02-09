# Bug Report

### Describe the bug

The `keyedDebounce` function is not triggering the callback when it should. After calling the debounced function with keys and arguments, the callback never gets invoked even after waiting for the debounce delay to pass.

### Reproduction

```js
const callback = (results) => {
  console.log('Callback triggered with:', results);
};

const debouncedFn = keyedDebounce(callback, 100);

// Call the debounced function
debouncedFn('key1', 'value1');
debouncedFn('key2', 'value2');

// Wait for debounce delay...
// Expected: callback should be called with { key1: ['value1'], key2: ['value2'] }
// Actual: callback is never called
```

### Expected behavior

The callback should be invoked after the debounce delay with all the accumulated results. Instead, nothing happens and the callback is never triggered.

### Additional context

This seems to have broken recently. The debounced function accepts the calls and waits the appropriate amount of time, but the callback just never fires. Not sure if this is related to a recent change in the codebase.

---
Repository: /testbed
