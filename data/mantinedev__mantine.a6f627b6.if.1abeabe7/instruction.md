# Bug Report

### Describe the bug

The `useLongPress` hook is not calling the `onStart` callback when a long press is initiated. The callback appears to be completely skipped even when provided.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press triggered'),
    {
      onStart: (event) => console.log('Long press started', event),
      onCancel: () => console.log('Long press cancelled'),
    }
  );

  return <button {...longPressHandlers}>Hold me</button>;
}
```

When holding down the button, the "Long press started" message never appears in the console, even though the long press itself works and triggers the main callback after the timeout.

### Expected behavior

The `onStart` callback should be invoked when the long press gesture begins (on mousedown/touchstart), before the timeout completes. This is useful for providing immediate visual feedback to users that their press has been registered.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
