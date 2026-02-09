# Bug Report

### Describe the bug

The `expectOpenedModal` test helper function is not working as expected. When I use it to verify that a modal is open in my tests, it passes even when the modal is clearly not rendered in the DOM.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { expectOpenedModal } from '@mantine-tests/dates';
import { Modal } from '@mantine/core';

// This test passes but shouldn't
const { container } = render(
  <Modal opened={false}>
    <div>Modal content</div>
  </Modal>
);

expectOpenedModal(container); // Should fail but passes
```

### Expected behavior

The `expectOpenedModal` helper should verify that a modal IS present in the document. Currently it seems to be checking the opposite - that the modal is NOT present. This makes it impossible to properly test modal visibility in date picker components.

### System Info
- @mantine/core version: latest
- @mantine/dates version: latest

---
Repository: /testbed
