# Bug Report

### Describe the bug

The `useLongPress` hook is not calling the `onCancel` callback when a long press is cancelled (e.g., when the user releases before the threshold is met or moves their pointer away). The callback should fire when the press is interrupted, but it's currently being skipped.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function Demo() {
  const longPressProps = useLongPress(
    () => console.log('Long press completed'),
    {
      onCancel: () => console.log('Long press cancelled'),
      threshold: 500
    }
  );

  return <button {...longPressProps}>Press and hold</button>;
}
```

Steps to reproduce:
1. Press and hold the button
2. Release before 500ms threshold
3. Check console

### Expected behavior

The `onCancel` callback should be called and log "Long press cancelled" to the console when the press is released early or cancelled.

### Actual behavior

Nothing is logged when releasing early. The `onCancel` callback is never invoked.

---
Repository: /testbed
