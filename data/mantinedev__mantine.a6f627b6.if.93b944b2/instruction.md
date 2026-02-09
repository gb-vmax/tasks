# Bug Report

### Describe the bug
When using `useThrottledCallback`, the throttled function stops working after the first call. Subsequent calls within the throttle window don't get queued or executed as expected.

### Reproduction
```js
import { useThrottledCallback } from '@mantine/hooks';

function MyComponent() {
  const throttledFn = useThrottledCallback((value) => {
    console.log('Called with:', value);
  }, 1000);

  // Call multiple times rapidly
  throttledFn('first');   // Works
  throttledFn('second');  // Should be queued but nothing happens
  throttledFn('third');   // Should be queued but nothing happens
  
  // After 1000ms, expect 'third' to be called but it never executes
}
```

### Expected behavior
The throttled callback should:
1. Execute immediately on first call
2. Queue subsequent calls during the throttle window
3. Execute the last queued call after the throttle period expires

Currently, only the first call works and subsequent calls are completely ignored instead of being queued for later execution.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
