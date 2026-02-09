# Bug Report

### Describe the bug

The `useLongPress` hook is not working properly - it seems like the cancel function is being triggered immediately on any mouse or touch event, preventing the long press from ever completing. The callback never fires even when holding down for the full duration.

### Reproduction

```jsx
import { useLongPress } from '@mantine/hooks';

function Demo() {
  const longPressHandlers = useLongPress(
    () => console.log('Long press completed!'),
    { threshold: 500 }
  );

  return (
    <button {...longPressHandlers}>
      Hold me for 500ms
    </button>
  );
}
```

Steps to reproduce:
1. Create a component with `useLongPress` hook
2. Try to hold down the button for the specified threshold duration
3. The callback never fires - seems like the press is being cancelled immediately

### Expected behavior

The callback should fire after holding the button for the specified threshold duration (500ms in the example). The long press should only be cancelled if the user releases or moves away before the threshold is reached.

### System Info
- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome/Firefox (happens on both)

---
Repository: /testbed
