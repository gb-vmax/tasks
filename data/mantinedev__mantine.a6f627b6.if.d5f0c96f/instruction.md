# Bug Report

### Describe the bug

The `useThrottledCallback` hook is not executing the callback function when it should. After the recent changes, the throttled callback seems to only set up the timeout but never actually calls the provided function, making the hook essentially non-functional.

### Reproduction

```js
import { useThrottledCallback } from '@mantine/hooks';

function MyComponent() {
  const [count, setCount] = useState(0);
  
  const throttledIncrement = useThrottledCallback(() => {
    setCount(c => c + 1);
    console.log('Callback executed');
  }, 1000);

  return (
    <button onClick={throttledIncrement}>
      Click me - Count: {count}
    </button>
  );
}
```

When clicking the button rapidly, the count never increments and "Callback executed" is never logged to the console. The throttling mechanism seems to be working (subsequent clicks are ignored during the wait period), but the actual callback function is never invoked.

### Expected behavior

The callback should execute immediately on the first call, and then be throttled for subsequent calls within the wait period. The count should increment and the console log should appear.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
