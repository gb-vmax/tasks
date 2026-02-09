# Bug Report

### Describe the bug

The `useLongPress` hook is not canceling properly on touch events. When I perform a long press using touch (on mobile or tablet), the cancel handler seems to be returning early and not properly cleaning up the long press state.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press triggered'),
    {
      onCancel: () => console.log('Long press canceled'),
      onFinish: () => console.log('Long press finished'),
      threshold: 500
    }
  );

  return (
    <div {...longPressHandlers}>
      Touch and hold me (on mobile/tablet)
    </div>
  );
}
```

Steps to reproduce:
1. Use the component on a touch device (mobile/tablet) or in browser dev tools with touch emulation
2. Touch and hold the element
3. Release before the threshold is met
4. The cancel/finish callbacks don't fire as expected

### Expected behavior

When a touch event is canceled (user releases touch before threshold), the `onCancel` or `onFinish` callbacks should be triggered properly. The hook should handle touch events the same way it handles mouse events.

### System Info
- @mantine/hooks version: latest
- Device: Mobile (iOS/Android) and touch emulation in Chrome DevTools

---
Repository: /testbed
