# Bug Report

### Describe the bug
Modal components are not being removed from the stack when closed. After closing a modal, it remains in the modal stack and continues to affect z-index calculations and potentially block interactions with other modals.

### Reproduction
```jsx
import { Modal, Button } from '@mantine/core';
import { useState } from 'react';

function App() {
  const [opened, setOpened] = useState(false);

  return (
    <>
      <Button onClick={() => setOpened(true)}>Open Modal</Button>
      <Modal opened={opened} onClose={() => setOpened(false)}>
        Modal content
      </Modal>
    </>
  );
}
```

Steps to reproduce:
1. Open a modal
2. Close the modal
3. Open another modal (or the same modal again)
4. The previous modal is still in the stack and affects the z-index

### Expected behavior
When a modal is closed, it should be properly removed from the modal stack. The stack should only contain currently open modals.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
