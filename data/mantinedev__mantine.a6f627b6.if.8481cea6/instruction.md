# Bug Report

### Describe the bug

The `useLongPress` hook is not working with touch events. When I try to use long press on a mobile device or touch screen, nothing happens. The callback is never triggered even though I'm holding down on the element.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press detected!');
  });

  return (
    <div {...longPressHandlers}>
      Touch and hold me on mobile
    </div>
  );
}
```

### Expected behavior

The long press callback should fire when the user touches and holds on a touch-enabled device. Currently it only seems to work with mouse events but completely ignores touch events.

### System Info
- @mantine/hooks version: latest
- Device: iPad / iPhone
- Browser: Safari Mobile

---
Repository: /testbed
