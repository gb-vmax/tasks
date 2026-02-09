# Bug Report

### Describe the bug

When using `useDebouncedCallback` with the `leading` option enabled, the callback behavior is incorrect after the first invocation. The leading edge execution only works once, and subsequent calls don't respect the leading edge behavior anymore.

### Reproduction

```js
const debouncedFn = useDebouncedCallback(
  () => {
    console.log('Called');
  },
  500,
  { leading: true }
);

// First call - executes immediately (correct)
debouncedFn();

// Wait for debounce to complete
await new Promise(resolve => setTimeout(resolve, 600));

// Second call - should execute immediately but doesn't
debouncedFn();
```

### Expected behavior

When `leading: true` is set, the callback should execute immediately on the first call of each debounce cycle. After the debounce period completes, the next invocation should again execute immediately on the leading edge.

Currently, only the very first call ever executes on the leading edge, and all subsequent calls (even after waiting for the debounce period) behave as if `leading: false`.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
