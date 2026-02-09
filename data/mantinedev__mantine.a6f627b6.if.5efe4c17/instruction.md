# Bug Report

### Describe the bug

The `useLongPress` hook is not triggering the long press callback anymore. After a recent update, the hook seems to be completely broken - it doesn't respond to mouse clicks or touch events at all.

### Reproduction

```tsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press detected!');
  });

  return (
    <div {...longPressHandlers}>
      Press and hold me
    </div>
  );
}
```

### Expected behavior

The callback should fire after holding down the mouse button or touch for the specified duration (default 500ms). Currently, nothing happens when you press and hold the element.

### Additional context

This was working fine before, but now the long press event never fires. I've tried with both mouse and touch events, and neither seem to work. The `onStart` callback also doesn't get called.

---
Repository: /testbed
