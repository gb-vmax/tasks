# Bug Report

### Describe the bug

The `useLongPress` hook is not properly handling touch events. When I try to use long press on touch devices, the cancel function seems to be terminating prematurely and the long press behavior doesn't work as expected.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press triggered'),
    {
      onFinish: () => console.log('Long press finished'),
      onCancel: () => console.log('Long press cancelled'),
      threshold: 500
    }
  );

  return (
    <div {...longPressHandlers}>
      Long press me on a touch device
    </div>
  );
}
```

When testing on mobile/touch devices:
1. Touch and hold the element
2. Release before the threshold
3. The cancel callback doesn't fire properly and the behavior is inconsistent

### Expected behavior

The hook should correctly handle both mouse and touch events. When a touch event is cancelled (finger lifted before threshold), the `onCancel` callback should be triggered and the long press should be properly terminated.

### System Info

- @mantine/hooks version: latest
- Device: iOS Safari, Android Chrome
- Also tested on desktop with touch emulation

---
Repository: /testbed
