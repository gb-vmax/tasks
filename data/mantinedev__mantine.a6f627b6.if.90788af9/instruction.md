# Bug Report

### Describe the bug

I'm experiencing an issue with `useThrottledCallback` where the callback is being invoked before the timeout is set. This causes the first call to execute immediately without any throttling, and subsequent calls within the wait period are not properly throttled.

### Reproduction

```js
import { useThrottledCallback } from '@mantine/hooks';

const [callback] = useThrottledCallback((value) => {
  console.log('Throttled:', value);
}, 1000);

// Call multiple times rapidly
callback('first');  // Executes immediately
callback('second'); // Should be throttled but timing is off
callback('third');  // Should be throttled but timing is off
```

### Expected behavior

The callback should be throttled properly with the timeout being set *before* the callback is invoked, ensuring that the throttling mechanism works correctly from the first call. The first invocation should respect the throttle timing, and subsequent calls within the wait period should be properly queued.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
