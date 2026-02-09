# Bug Report

### Describe the bug

The `useLongPress` hook is throwing an error when the `onStart` callback is not provided. It seems like the hook is trying to call `onStart` even when it's undefined, which causes the application to crash.

### Reproduction

```tsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPress = useLongPress(
    () => console.log('Long press triggered'),
    {
      threshold: 500,
      // onStart is not provided
    }
  );

  return <button {...longPress}>Press me</button>;
}
```

When pressing the button, the app crashes with:
```
TypeError: onStart is not a function
```

### Expected behavior

The hook should work fine when `onStart` is not provided, as it's an optional callback. Only the main callback and `onCancel` should be required (if specified in options).

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
