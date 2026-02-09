# Bug Report

### Describe the bug

The `useFocusReturn` hook is not working properly - focus is never returned to the previously focused element when a modal/overlay closes. After closing a modal, the focus just disappears instead of returning to the element that was focused before the modal opened.

### Reproduction

```jsx
import { useFocusReturn } from '@mantine/hooks';

function MyModal({ opened, onClose }) {
  useFocusReturn({ opened });
  
  return opened ? (
    <div>
      <button onClick={onClose}>Close</button>
      <input placeholder="Focus stays here" />
    </div>
  ) : null;
}

// Usage:
// 1. Focus on a button or input
// 2. Open the modal
// 3. Close the modal
// Expected: Focus returns to the original element
// Actual: Focus is lost completely
```

### Expected behavior

When the modal closes, focus should automatically return to the element that was focused before the modal opened. This is important for keyboard navigation and accessibility.

### System Info

- @mantine/hooks version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
