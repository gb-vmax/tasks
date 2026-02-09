# Bug Report

### Describe the bug

I'm experiencing an issue with the modal stack functionality after a recent update. When opening a modal, it seems to behave in the opposite way - modals that should be open appear closed, and the state management is completely inverted.

### Reproduction

```jsx
import { useModalsStack } from '@mantine/core';

function MyComponent() {
  const modals = useModalsStack(['modal1', 'modal2']);
  
  // Try to open modal1
  modals.open('modal1');
  
  // Expected: modal1 should be opened
  // Actual: modal1 remains closed
  
  const { opened } = modals.register('modal1');
  console.log(opened); // Shows false when it should be true
}
```

### Expected behavior

When calling `modals.open('modal1')`, the modal should open and `register('modal1').opened` should return `true`. Instead, the opened state appears to be inverted - modals that should be open are reported as closed.

Additionally, when `allowMultiple` is false (single modal mode), opening a new modal should close other modals and open the new one, but the behavior seems incorrect.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This is blocking our modal implementation as none of our modals can be opened properly. Any help would be appreciated!

---
Repository: /testbed
