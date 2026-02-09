# Bug Report

### Describe the bug

The `useLongPress` hook is calling the `onCancel` callback even when it's not provided. This causes a runtime error when the hook is used without an `onCancel` callback.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press detected');
  });

  return (
    <button {...longPressHandlers}>
      Press and hold me
    </button>
  );
}
```

When you press and release the button before the long press threshold, the app crashes with:

```
TypeError: onCancel is not a function
```

### Expected behavior

The hook should only call `onCancel` if it's actually provided as an option. When `onCancel` is not defined, releasing the button early should simply do nothing without throwing an error.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
