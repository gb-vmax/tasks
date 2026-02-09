# Bug Report

### Describe the bug

The `keyedDebounce` function is not working correctly after a recent update. When calling the debounced function multiple times with the same key, only the last set of arguments is preserved instead of accumulating all the arguments that were passed.

### Reproduction

```js
const debounced = keyedDebounce((results) => {
  console.log(results);
}, 100);

debounced('key1', 'arg1', 'arg2');
debounced('key1', 'arg3', 'arg4');
debounced('key1', 'arg5', 'arg6');

// After debounce fires, expected output:
// { key1: ['arg1', 'arg2', 'arg3', 'arg4', 'arg5', 'arg6'] }

// Actual output:
// { key1: ['arg5', 'arg6'] }
```

### Expected behavior

When the debounced function is called multiple times with the same key before the timeout fires, all arguments should be accumulated in an array for that key. The callback should receive all the arguments that were passed during the debounce window, not just the last call's arguments.

### Additional context

This appears to have broken after a recent change. Previously, calling the debounced function multiple times would collect all arguments, but now it seems like each call is overwriting the previous arguments instead of appending to them.

---
Repository: /testbed
