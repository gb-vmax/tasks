# Bug Report

### Describe the bug

The `useLongPress` hook's `onStart` callback is not being triggered when it should be. After a recent update, the callback only fires under very specific conditions that don't make sense for normal usage.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press detected'),
    {
      onStart: (event) => console.log('Press started', event),
      threshold: 500
    }
  );

  return <button {...longPressHandlers()}>Press and hold me</button>;
}
```

When pressing the button, the `onStart` callback doesn't fire even though the press is registered. It seems like the callback is being blocked by some condition that checks the event object.

### Expected behavior

The `onStart` callback should be called whenever a press starts, regardless of the event object's properties. The callback was working fine before and should trigger on any valid press event (mouse down, touch start, etc.).

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
