# Bug Report

### Describe the bug

When using `useDebouncedCallback` with the `leading` option enabled, the leading call only fires once and subsequent calls don't trigger the leading behavior anymore. After the first leading call executes, the debounced function stops invoking the callback at the leading edge even after the debounce period has elapsed.

### Reproduction

```js
const debouncedFn = useDebouncedCallback(
  () => {
    console.log('Called');
  },
  500,
  { leading: true }
);

// First call - executes immediately (leading edge) ✓
debouncedFn();

// Wait for debounce period to complete
setTimeout(() => {
  // Second call - should execute immediately (leading edge) but doesn't ✗
  debouncedFn();
}, 1000);
```

### Expected behavior

The callback should execute immediately on the leading edge for each new sequence of calls after the debounce period has elapsed. The leading behavior should reset after the timeout completes, allowing subsequent calls to also trigger at the leading edge.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
