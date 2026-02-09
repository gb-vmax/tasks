# Bug Report

### Describe the bug

The `useLongPress` hook is calling the `onFinish` callback at the wrong time. When a long press is successfully completed, the `onFinish` callback is being triggered even though it should only be called when the press is released before the threshold is met.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function Demo() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press activated'),
    {
      onFinish: () => console.log('Finished - released before threshold'),
      onCancel: () => console.log('Cancelled - released after threshold'),
      threshold: 500,
    }
  );

  return <button {...longPressHandlers}>Press and hold</button>;
}
```

**Steps to reproduce:**
1. Press and hold the button for more than 500ms (threshold time)
2. Release the button
3. Check the console output

**Actual behavior:**
Both "Long press activated" and "Finished - released before threshold" are logged, which is incorrect.

**Expected behavior:**
Only "Long press activated" and "Cancelled - released after threshold" should be logged. The `onFinish` callback should NOT be called when a long press was successfully activated - it should only be called when the press is released BEFORE reaching the threshold.

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
