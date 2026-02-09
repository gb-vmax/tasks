# Bug Report

### Describe the bug

The `register` function in the modals stack is returning the wrong `opened` state. When registering a modal that exists in the stack, it returns `opened: false`, but it should return `opened: true`. This causes modals to be closed when they should be open.

### Reproduction

```tsx
import { useDisclosureStack } from '@mantine/core';

function MyComponent() {
  const { open, register } = useDisclosureStack();
  
  // Open a modal
  open('modal-1');
  
  // Register the same modal
  const { opened } = register('modal-1');
  
  console.log(opened); // Expected: true, Actual: false
}
```

### Expected behavior

When a modal ID is in the stack (meaning it's open), the `register` function should return `opened: true`. Currently it's doing the opposite - returning `false` when the modal is in the stack and `true` when it's not.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
