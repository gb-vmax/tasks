# Bug Report

### Describe the bug

The `useLongPress` hook stopped working with touch events. When I try to use long press on mobile devices or touch screens, nothing happens - the callback never fires.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press detected');
  });

  return (
    <div {...longPressHandlers}>
      Touch and hold me
    </div>
  );
}
```

When testing on a mobile device or using touch events in Chrome DevTools:
1. Touch and hold the element
2. Nothing happens - the callback is never triggered
3. Only mouse events seem to work now

### Expected behavior

Both mouse events and touch events should trigger the long press callback. This used to work fine before, but now it only responds to mouse events and completely ignores touch events.

### System Info
- @mantine/hooks version: latest
- Device: iOS Safari, Android Chrome
- Also reproducible in Chrome DevTools with touch emulation enabled

---
Repository: /testbed
