# Bug Report

### Describe the bug

I'm experiencing an issue with `useThrottledCallback` where the throttling behavior seems broken. The callback is being executed immediately every time instead of being properly throttled with the specified wait time.

### Reproduction

```js
import { useThrottledCallback } from '@mantine/hooks';

function MyComponent() {
  const throttledFn = useThrottledCallback((value) => {
    console.log('Throttled:', value, Date.now());
  }, 1000);

  const handleClick = () => {
    // These should be throttled to execute once per second
    throttledFn('call 1');
    throttledFn('call 2');
    throttledFn('call 3');
  };

  return <button onClick={handleClick}>Click me</button>;
}
```

### Expected behavior

When clicking the button, the throttled function should only execute once within the 1000ms window, with subsequent calls within that window being ignored or queued. Instead, all calls seem to execute immediately without any throttling.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

The throttling mechanism doesn't seem to be working as intended - it's like the timeout is being cleared immediately after being set, defeating the purpose of throttling.

---
Repository: /testbed
