# Bug Report

### Describe the bug

The `useLongPress` hook is not passing the event object to the `onCancel` callback when a long press is cancelled. This breaks functionality when you need access to the event in the cancel handler.

### Reproduction

```tsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPress = useLongPress(
    () => console.log('Long press triggered'),
    {
      onCancel: (event) => {
        // event is undefined here, but should contain the mouse/touch event
        console.log('Cancelled at:', event.clientX, event.clientY);
      }
    }
  );

  return <button {...longPress}>Press and hold</button>;
}
```

### Expected behavior

When a long press is cancelled (e.g., user moves their finger/mouse before the threshold is reached), the `onCancel` callback should receive the event object as a parameter, similar to how `onFinish` receives it.

### Current behavior

The `onCancel` callback is being invoked without any arguments, making it impossible to access event properties like coordinates, target element, etc.

---
Repository: /testbed
