# Bug Report

### Describe the bug

The `expectOpenedModal` helper function is not correctly detecting when a modal is open. When I call this helper to verify that a modal has been opened, it's giving false positives - the assertion passes even when the modal is actually closed.

### Reproduction

```tsx
import { expectOpenedModal } from '@mantine-tests/dates';

// Open a modal component
openModal();

// This should pass but currently fails
expectOpenedModal(container);
```

The helper seems to be checking for the wrong condition. When a modal is supposed to be open, the test helper reports that it's closed.

### Expected behavior

`expectOpenedModal` should correctly verify that a modal is present in the DOM when it's actually opened. The assertion should pass when the modal is visible and fail when it's not.

### System Info
- @mantine/core version: latest
- Testing library: @testing-library/react

---
Repository: /testbed
