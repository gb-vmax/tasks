# Bug Report

### Describe the bug

When using Modal components, the body ID is not being returned correctly in certain scenarios. The `useModalBodyId` hook appears to return `undefined` instead of the expected body ID value, which breaks accessibility attributes and ARIA relationships.

### Reproduction

```tsx
import { Modal } from '@mantine/core';

function MyModal() {
  return (
    <Modal opened={true} onClose={() => {}}>
      <Modal.Body>
        Content here
      </Modal.Body>
    </Modal>
  );
}
```

When the modal is rendered, the body element doesn't get the proper ID attribute assigned. Inspecting the DOM shows that the ID is missing or undefined.

### Expected behavior

The `useModalBodyId` hook should consistently return the body ID so that it can be properly assigned to the modal body element for accessibility purposes. The modal should have proper ARIA attributes linking the title and body.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
