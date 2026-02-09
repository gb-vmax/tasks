# Bug Report

### Describe the bug

The `useLongPress` hook is not triggering on touch events anymore. When I try to use long press on mobile devices or touch-enabled screens, nothing happens. Mouse events still work fine on desktop, but touch events are completely broken.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press triggered!');
  });

  return (
    <div {...longPressHandlers}>
      Long press me on mobile
    </div>
  );
}
```

Steps to reproduce:
1. Use the `useLongPress` hook on a component
2. Try to long press on a touch device (mobile phone, tablet, or touch screen)
3. The callback never fires

### Expected behavior

The long press callback should trigger after holding down on the element for the specified duration, regardless of whether it's a mouse event or touch event. Both mouse and touch interactions should be supported.

### System Info
- @mantine/hooks version: latest
- Device: iOS Safari, Android Chrome
- Also tested on Chrome DevTools mobile emulation

This was working fine before, not sure what changed. Mouse events still work on desktop but touch is completely non-functional now.

---
Repository: /testbed
