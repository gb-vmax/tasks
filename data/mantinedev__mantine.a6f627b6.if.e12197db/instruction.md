# Bug Report

### Describe the bug

The `useLongPress` hook is not behaving correctly when handling the end of a press interaction. After a long press completes and `onFinish` is called, subsequent quick taps are incorrectly triggering the `onCancel` callback instead of being handled normally.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press activated'),
    {
      onFinish: () => console.log('Long press finished'),
      onCancel: () => console.log('Press cancelled'),
      threshold: 500
    }
  );

  return <button {...longPressHandlers}>Press and hold me</button>;
}
```

Steps to reproduce:
1. Press and hold the button for more than 500ms (long press threshold)
2. Release the button - "Long press finished" is logged correctly
3. Immediately tap the button quickly (without holding)
4. "Press cancelled" is logged unexpectedly

### Expected behavior

After completing a long press and releasing, a subsequent quick tap should not trigger the `onCancel` callback. The `onCancel` should only fire when a press is started but released before reaching the threshold, not after a successful long press has already completed.

### System Info

- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
