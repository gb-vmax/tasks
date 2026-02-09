# Bug Report

### Describe the bug
The `useLongPress` hook's `onStart` callback is not being triggered when a long press is initiated. It seems like the callback is completely broken and nothing happens when the press starts.

### Reproduction
```jsx
import { useLongPress } from '@mantine/hooks';

function MyComponent() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press triggered'),
    {
      onStart: (event) => console.log('Press started', event),
      onCancel: () => console.log('Press cancelled')
    }
  );

  return <button {...longPressHandlers}>Press and hold me</button>;
}
```

When pressing and holding the button, the `onStart` callback never fires. Expected to see "Press started" logged to console along with the event object, but nothing happens.

### Expected behavior
The `onStart` callback should be called when the press begins, receiving the event object as a parameter.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
