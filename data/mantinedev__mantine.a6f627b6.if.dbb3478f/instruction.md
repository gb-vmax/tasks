# Bug Report

### Describe the bug

The `useLongPress` hook stopped working with mouse events. When I try to trigger a long press using mouse clicks, nothing happens - the callback is never fired. Touch events seem unaffected.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press detected!');
  });

  return (
    <button {...longPressHandlers}>
      Hold me down with mouse
    </button>
  );
}
```

### Expected behavior

The long press callback should fire when holding down the mouse button on the element for the specified duration (default 500ms). Currently, it only works with touch events but not with mouse events.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
