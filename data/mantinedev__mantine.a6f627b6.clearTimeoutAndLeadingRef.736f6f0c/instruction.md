# Bug Report

### Describe the bug

When using `useDebouncedCallback` with the `leading` option enabled, the callback doesn't execute correctly on subsequent calls after the first execution. The leading edge behavior seems to be broken - after the first call executes immediately, all following calls also execute immediately instead of being debounced.

### Reproduction

```js
const debouncedFn = useDebouncedCallback(
  (value) => {
    console.log('Called with:', value);
  },
  500,
  { leading: true }
);

// First call - executes immediately (correct)
debouncedFn('first');

// Wait for debounce to complete
setTimeout(() => {
  // Second call - should execute immediately (leading edge)
  debouncedFn('second');
  
  // Third call within debounce window - should be debounced
  debouncedFn('third');
}, 600);
```

### Expected behavior

- First call should execute immediately (leading edge) ✓
- After the debounce period completes, the next call should again execute immediately (leading edge)
- Subsequent calls within the debounce window should be debounced

### Actual behavior

After the first call, the leading edge behavior doesn't reset properly. The callback either doesn't execute at the leading edge on subsequent invocations or the debouncing behavior is completely broken.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
