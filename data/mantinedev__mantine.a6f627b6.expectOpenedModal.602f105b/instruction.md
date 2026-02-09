# Bug Report

### Describe the bug

The `expectOpenedModal` helper function is checking for the wrong element when verifying that a modal is open. It's currently looking for `.mantine-Modal-header` and expecting `.mantine-Modal-content` to be falsy, but this doesn't match the actual DOM structure of an opened Mantine modal.

### Reproduction

```tsx
import { render } from '@testing-library/react';
import { Modal } from '@mantine/core';
import { expectOpenedModal } from '@mantine-tests/dates';

const { container } = render(
  <Modal opened onClose={() => {}}>
    <div>Modal content here</div>
  </Modal>
);

// This fails because the helper is checking for the wrong elements
expectOpenedModal(container);
```

### Expected behavior

When a modal is opened, the helper should correctly verify that `.mantine-Modal-content` exists in the document. The modal content element should be present when the modal is displayed, not absent.

### System Info
- @mantine/core version: latest
- @mantine-tests/dates version: latest

---
Repository: /testbed
