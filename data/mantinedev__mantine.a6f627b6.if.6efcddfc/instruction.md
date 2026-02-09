# Bug Report

### Describe the bug

The `useLongPress` hook is not working properly - the long press callback never fires when holding down on an element. It seems like the cancel function is being triggered immediately on mouse/touch events, preventing the long press from completing.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function Demo() {
  const longPressHandlers = useLongPress(() => {
    console.log('Long press triggered!');
  });

  return (
    <button {...longPressHandlers}>
      Hold me for 500ms
    </button>
  );
}
```

### Expected behavior

When holding down the button for 500ms (or the configured threshold), the callback should be executed and "Long press triggered!" should be logged to the console.

### Actual behavior

The callback never fires, no matter how long you hold down the button. The long press action appears to be cancelled immediately.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
